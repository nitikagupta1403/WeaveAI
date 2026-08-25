"""Interactive pre-outcome garment/text bounding-box annotator.

The tool never imports DINOv2, extracts learned features, fits a classifier, or
computes an outcome. Coordinates are stored in original-image pixels.
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

import pandas as pd
from PIL import Image, ImageOps, ImageTk

from annotation_mask_audit import multi_structure_box
from preprocess_audit import load_polarity_normalized_grayscale


TOOL_VERSION = 1
CANVAS_WIDTH = 1100
CANVAS_HEIGHT = 760
BOX_COLOURS = {
    "proposal": "#ff9800",
    "garment": "#00a651",
    "text": "#d62728",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--source-manifest", type=Path, required=True)
    parser.add_argument("--output-jsonl", type=Path, required=True)
    parser.add_argument(
        "--selection-csv",
        type=Path,
        help="Optional CSV containing a relative_path column for a pilot subset.",
    )
    return parser.parse_args()


def atomic_write_jsonl(path: Path, records: dict[str, dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    ordered = sorted(records.values(), key=lambda item: int(item["row_index"]))
    with temporary.open("w", encoding="utf-8") as stream:
        for record in ordered:
            stream.write(json.dumps(record, sort_keys=True) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def load_existing(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    records: dict[str, dict] = {}
    with path.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            relative_path = record["relative_path"]
            if relative_path in records:
                raise RuntimeError(
                    f"Duplicate annotation for {relative_path} at line {line_number}"
                )
            records[relative_path] = record
    return records


def clamp_box(box: list[int], width: int, height: int) -> list[int]:
    left, top, right, bottom = box
    left, right = sorted((max(0, min(width, left)), max(0, min(width, right))))
    top, bottom = sorted((max(0, min(height, top)), max(0, min(height, bottom))))
    if right <= left or bottom <= top:
        raise ValueError("Bounding box must have positive area")
    return [left, top, right, bottom]


class Annotator:
    def __init__(
        self,
        root: tk.Tk,
        data_root: Path,
        rows: list[dict],
        output_jsonl: Path,
    ) -> None:
        self.root = root
        self.data_root = data_root
        self.rows = rows
        self.output_jsonl = output_jsonl
        self.annotations = load_existing(output_jsonl)
        self.position = 0
        self.mode = "garment"
        self.drag_start: tuple[int, int] | None = None
        self.temporary_rectangle: int | None = None
        self.current_image: Image.Image | None = None
        self.current_array = None
        self.tk_image = None
        self.display_scale = 1.0
        self.display_left = 0
        self.display_top = 0
        self.garment_box: list[int] | None = None
        self.proposed_garment_box: list[int] | None = None
        self.text_boxes: list[list[int]] = []
        self.ambiguous = False
        self.existing_reviewed = False

        root.title("Experiment 08 — Pre-outcome dual-box annotation")
        self.status = tk.StringVar()
        self.instructions = tk.StringVar(
            value=(
                "G: garment mode | T: text mode | A: accept proposal | "
                "U: undo text | C: clear | F: ambiguity | S: save | "
                "N/Right: save+next | P/Left: previous | Q: quit"
            )
        )

        tk.Label(root, textvariable=self.status, anchor="w").pack(fill="x")
        tk.Label(root, textvariable=self.instructions, anchor="w").pack(fill="x")
        self.canvas = tk.Canvas(
            root,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            bg="#303030",
            highlightthickness=0,
        )
        self.canvas.pack()

        controls = tk.Frame(root)
        controls.pack(fill="x")
        for label, command in [
            ("Garment [G]", lambda: self.set_mode("garment")),
            ("Text [T]", lambda: self.set_mode("text")),
            ("Accept proposal [A]", self.accept_proposal),
            ("Accept + next [Return]", self.accept_and_next),
            ("Undo text [U]", self.undo_text),
            ("Clear [C]", self.clear_boxes),
            ("Toggle ambiguity [F]", self.toggle_ambiguity),
            ("Previous [P]", self.previous),
            ("Save [S]", self.save),
            ("Save + next [N]", self.next),
        ]:
            tk.Button(controls, text=label, command=command).pack(
                side="left", padx=2, pady=3
            )

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        for key, callback in {
            "g": lambda _event: self.set_mode("garment"),
            "t": lambda _event: self.set_mode("text"),
            "a": lambda _event: self.accept_proposal(),
            "u": lambda _event: self.undo_text(),
            "c": lambda _event: self.clear_boxes(),
            "f": lambda _event: self.toggle_ambiguity(),
            "s": lambda _event: self.save(),
            "n": lambda _event: self.next(),
            "p": lambda _event: self.previous(),
            "<Return>": lambda _event: self.accept_and_next(),
            "<Right>": lambda _event: self.next(),
            "<Left>": lambda _event: self.previous(),
            "q": lambda _event: self.quit(),
        }.items():
            root.bind(key, callback)
        root.protocol("WM_DELETE_WINDOW", self.quit)
        self.load_position(0)

    def record(self) -> dict:
        return self.rows[self.position]

    def load_position(self, position: int) -> None:
        if not (0 <= position < len(self.rows)):
            return
        self.position = position
        self.mode = "garment"
        row = self.record()
        path = self.data_root / row["relative_path"]
        self.current_image = Image.open(path).convert("L")
        self.current_array, _ = load_polarity_normalized_grayscale(path)
        width, height = self.current_image.size

        left, top, right, bottom, _ = multi_structure_box(self.current_array)
        self.proposed_garment_box = [left, top, right, bottom]

        existing = self.annotations.get(row["relative_path"])
        if existing is None:
            self.garment_box = None
            self.text_boxes = []
            self.ambiguous = False
            self.existing_reviewed = False
        else:
            if existing["source_sha256"] != row["sha256"]:
                raise RuntimeError(
                    f"Source hash changed for {row['relative_path']}"
                )
            self.garment_box = existing.get("garment_box")
            self.text_boxes = existing.get("text_boxes", [])
            self.ambiguous = bool(existing.get("ambiguous", False))
            self.existing_reviewed = bool(existing.get("reviewed", False))
        self.render()

    def render(self) -> None:
        assert self.current_image is not None
        self.canvas.delete("all")
        preview = ImageOps.autocontrast(self.current_image)
        width, height = preview.size
        self.display_scale = min(
            (CANVAS_WIDTH - 30) / width,
            (CANVAS_HEIGHT - 30) / height,
        )
        display_size = (
            max(1, round(width * self.display_scale)),
            max(1, round(height * self.display_scale)),
        )
        preview = preview.resize(display_size, Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(preview)
        self.display_left = (CANVAS_WIDTH - display_size[0]) // 2
        self.display_top = (CANVAS_HEIGHT - display_size[1]) // 2
        self.canvas.create_image(
            self.display_left,
            self.display_top,
            image=self.tk_image,
            anchor="nw",
        )

        if self.garment_box is None and self.proposed_garment_box is not None:
            self.draw_box(
                self.proposed_garment_box,
                BOX_COLOURS["proposal"],
                dash=(6, 4),
                width=2,
            )
        elif self.garment_box is not None:
            self.draw_box(
                self.garment_box, BOX_COLOURS["garment"], width=3
            )
        for box in self.text_boxes:
            self.draw_box(box, BOX_COLOURS["text"], width=3)

        row = self.record()
        reviewed = sum(
            bool(item.get("reviewed", False))
            for item in self.annotations.values()
        )
        flag = " | AMBIGUOUS" if self.ambiguous else ""
        saved = "saved" if self.existing_reviewed else "unsaved/unreviewed"
        self.status.set(
            f"{self.position + 1}/{len(self.rows)} | reviewed={reviewed} | "
            f"mode={self.mode.upper()} | {saved}{flag} | "
            f"{row['garment_id']} | {row['relative_path']}"
        )

    def draw_box(
        self,
        box: list[int],
        colour: str,
        dash: tuple[int, int] | None = None,
        width: int = 2,
    ) -> None:
        left, top, right, bottom = box
        self.canvas.create_rectangle(
            self.display_left + left * self.display_scale,
            self.display_top + top * self.display_scale,
            self.display_left + right * self.display_scale,
            self.display_top + bottom * self.display_scale,
            outline=colour,
            width=width,
            dash=dash,
        )

    def canvas_to_image(self, x: int, y: int) -> tuple[int, int]:
        assert self.current_image is not None
        width, height = self.current_image.size
        image_x = round((x - self.display_left) / self.display_scale)
        image_y = round((y - self.display_top) / self.display_scale)
        return (
            max(0, min(width, image_x)),
            max(0, min(height, image_y)),
        )

    def on_press(self, event: tk.Event) -> None:
        self.drag_start = self.canvas_to_image(event.x, event.y)
        colour = BOX_COLOURS[self.mode]
        self.temporary_rectangle = self.canvas.create_rectangle(
            event.x, event.y, event.x, event.y, outline=colour, width=3
        )

    def on_drag(self, event: tk.Event) -> None:
        if self.temporary_rectangle is not None:
            start = self.drag_start
            assert start is not None
            x0 = self.display_left + start[0] * self.display_scale
            y0 = self.display_top + start[1] * self.display_scale
            self.canvas.coords(
                self.temporary_rectangle, x0, y0, event.x, event.y
            )

    def on_release(self, event: tk.Event) -> None:
        if self.drag_start is None:
            return
        assert self.current_image is not None
        end = self.canvas_to_image(event.x, event.y)
        width, height = self.current_image.size
        try:
            box = clamp_box(
                [
                    self.drag_start[0],
                    self.drag_start[1],
                    end[0],
                    end[1],
                ],
                width,
                height,
            )
        except ValueError:
            self.drag_start = None
            self.render()
            return
        if self.mode == "garment":
            self.garment_box = box
        else:
            self.text_boxes.append(box)
        self.existing_reviewed = False
        self.drag_start = None
        self.temporary_rectangle = None
        self.render()

    def set_mode(self, mode: str) -> None:
        self.mode = mode
        self.render()

    def accept_proposal(self) -> None:
        if self.proposed_garment_box is not None:
            self.garment_box = list(self.proposed_garment_box)
            self.existing_reviewed = False
            self.render()

    def accept_and_next(self) -> None:
        """Accept the proposal and advance only for a clean, no-text case."""
        if self.text_boxes or self.ambiguous:
            messagebox.showwarning(
                "Existing review marks",
                "Use Save + next when text boxes or ambiguity are present.",
            )
            return
        self.accept_proposal()
        self.next()

    def undo_text(self) -> None:
        if self.text_boxes:
            self.text_boxes.pop()
            self.existing_reviewed = False
            self.render()

    def clear_boxes(self) -> None:
        self.garment_box = None
        self.text_boxes = []
        self.ambiguous = False
        self.existing_reviewed = False
        self.render()

    def toggle_ambiguity(self) -> None:
        self.ambiguous = not self.ambiguous
        self.existing_reviewed = False
        self.render()

    def save(self) -> bool:
        if self.garment_box is None:
            messagebox.showwarning(
                "Garment box required",
                "Draw or accept the garment box before saving.",
            )
            return False
        row = self.record()
        self.annotations[row["relative_path"]] = {
            "tool_version": TOOL_VERSION,
            "row_index": int(row["row_index"]),
            "relative_path": row["relative_path"],
            "source_sha256": row["sha256"],
            "category": row["category"],
            "garment_id": row["garment_id"],
            "fold_id": int(row["fold_id"]),
            "image_width": int(self.current_image.size[0]),
            "image_height": int(self.current_image.size[1]),
            "garment_box": [int(value) for value in self.garment_box],
            "text_boxes": [
                [int(value) for value in box] for box in self.text_boxes
            ],
            "ambiguous": bool(self.ambiguous),
            "reviewed": True,
            "reviewed_at_utc": datetime.now(timezone.utc).isoformat(),
            "decision_basis": "visual garment/text localization only; no learned feature or classifier outcome",
        }
        atomic_write_jsonl(self.output_jsonl, self.annotations)
        self.existing_reviewed = True
        self.render()
        return True

    def next(self) -> None:
        if self.save() and self.position + 1 < len(self.rows):
            self.load_position(self.position + 1)

    def previous(self) -> None:
        if self.position > 0:
            self.load_position(self.position - 1)

    def quit(self) -> None:
        if messagebox.askyesno(
            "Quit annotator",
            "Quit now? Saved annotations will be preserved.",
        ):
            self.root.destroy()


def load_rows(
    source_manifest: Path, selection_csv: Path | None
) -> list[dict]:
    manifest = pd.read_csv(source_manifest, keep_default_na=False)
    required = {
        "row_index",
        "relative_path",
        "sha256",
        "category",
        "garment_id",
        "fold_id",
    }
    missing = required.difference(manifest.columns)
    if missing:
        raise RuntimeError(f"Source manifest lacks columns: {sorted(missing)}")
    if selection_csv is not None:
        selection = pd.read_csv(selection_csv, keep_default_na=False)
        if "relative_path" not in selection.columns:
            raise RuntimeError("Selection CSV requires relative_path")
        requested = selection["relative_path"].tolist()
        if len(requested) != len(set(requested)):
            raise RuntimeError("Selection CSV contains duplicate paths")
        ordered = pd.DataFrame(
            {
                "relative_path": requested,
                "_selection_order": range(len(requested)),
            }
        )
        manifest = ordered.merge(
            manifest,
            on="relative_path",
            how="left",
            validate="one_to_one",
        )
        if manifest["sha256"].eq("").any() or manifest["sha256"].isna().any():
            raise RuntimeError("Selection CSV contains paths absent from manifest")
        manifest = manifest.sort_values("_selection_order")
    else:
        manifest = manifest.sort_values("row_index")
    return manifest.to_dict(orient="records")


def main() -> None:
    args = parse_args()
    rows = load_rows(args.source_manifest, args.selection_csv)
    if not rows:
        raise RuntimeError("No images selected")
    root = tk.Tk()
    Annotator(root, args.data_root, rows, args.output_jsonl)
    root.mainloop()


if __name__ == "__main__":
    main()
