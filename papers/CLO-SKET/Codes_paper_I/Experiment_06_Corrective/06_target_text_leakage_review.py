"""Visual target-text leakage audit for the frozen CLEAN image field.

This is a POST-OUTCOME INPUT-INTEGRITY AUDIT only.

It does NOT fit a classifier, compute predictions, inspect model errors, modify
images, or rerun Experiment 06. It verifies the frozen CLEAN PNG hash for every
row before review and provides a resumable human-review interface.

Review labels are frozen by TARGET_TEXT_LEAKAGE_AUDIT_LOCK.md:
    NONE
    EXACT
    PARTIAL_OR_ABBREVIATED
    AMBIGUOUS

Keyboard controls:
    Space / n : NONE and advance
    e         : EXACT and advance
    p         : PARTIAL_OR_ABBREVIATED and advance
    a         : AMBIGUOUS and advance
    o         : toggle other_text_visible for current row
    b         : go back one row
    q         : save and quit

The true category is shown OUTSIDE the image tile for comparison. It is not part
of the CLEAN image and must never be interpreted as image content.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

import pandas as pd
from PIL import Image, ImageTk


EXPECTED_ROWS = 2300
VALID_STATUSES = {
    "NONE",
    "EXACT",
    "PARTIAL_OR_ABBREVIATED",
    "AMBIGUOUS",
}

REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_STATUS = (
    REPO_ROOT
    / "papers/CLO-SKET/evidence/Experiment_06_Corrective/"
    / "experiment06_annotation_status.csv"
)
DEFAULT_REVIEW = (
    REPO_ROOT
    / "papers/CLO-SKET/evidence/Experiment_06_Corrective/"
    / "experiment06_target_text_leakage_review.csv"
)
DEFAULT_SUMMARY = (
    REPO_ROOT
    / "papers/CLO-SKET/evidence/Experiment_06_Corrective/"
    / "experiment06_target_text_leakage_summary.json"
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--clean-root",
        type=Path,
        required=True,
        help=(
            "Frozen Experiment-08 materialized-v4 root containing "
            "images/0000.png ... images/2299.png."
        ),
    )
    p.add_argument("--annotation-status", type=Path, default=DEFAULT_STATUS)
    p.add_argument("--review-csv", type=Path, default=DEFAULT_REVIEW)
    p.add_argument("--summary-json", type=Path, default=DEFAULT_SUMMARY)
    p.add_argument(
        "--verify-only",
        action="store_true",
        help="Verify all 2,300 CLEAN PNG hashes and exit without opening the GUI.",
    )
    p.add_argument(
        "--finalize",
        action="store_true",
        help=(
            "Validate that all 2,300 rows have a completed review status and "
            "write the frozen audit summary. No GUI is opened."
        ),
    )
    return p.parse_args()


def load_authoritative_status(path: Path, clean_root: Path) -> pd.DataFrame:
    frame = pd.read_csv(path, keep_default_na=False)

    required = {
        "row_index",
        "relative_path",
        "category",
        "corrected_garment_id",
        "corrected_fold_id",
        "clean_image_relative_path",
        "clean_png_sha256",
    }
    missing = required.difference(frame.columns)
    if missing:
        raise RuntimeError(
            "Annotation-status table missing columns: "
            + ", ".join(sorted(missing))
        )

    if len(frame) != EXPECTED_ROWS:
        raise RuntimeError(f"Expected {EXPECTED_ROWS} rows, found {len(frame)}")

    frame = frame.sort_values("row_index").reset_index(drop=True)
    if frame["row_index"].astype(int).tolist() != list(range(EXPECTED_ROWS)):
        raise RuntimeError("row_index must be exactly 0..2299")

    print("Verifying all frozen CLEAN PNG hashes before review...")
    for i, row in enumerate(frame.itertuples(index=False), start=1):
        path_i = clean_root / row.clean_image_relative_path
        if not path_i.is_file():
            raise RuntimeError(f"Missing CLEAN image: {path_i}")

        observed = sha256_file(path_i)
        if observed != row.clean_png_sha256:
            raise RuntimeError(
                f"CLEAN PNG SHA mismatch for row {row.row_index}: "
                f"{observed} != {row.clean_png_sha256}"
            )

        if i % 250 == 0 or i == EXPECTED_ROWS:
            print(f"CLEAN hash verification: {i}/{EXPECTED_ROWS}")

    print("Frozen CLEAN PNG verification: PASS")
    return frame


def initialize_or_load_review(
    authoritative: pd.DataFrame,
    review_path: Path,
) -> pd.DataFrame:
    base = authoritative[
        [
            "row_index",
            "relative_path",
            "category",
            "corrected_garment_id",
            "corrected_fold_id",
            "clean_image_relative_path",
            "clean_png_sha256",
        ]
    ].copy()

    if review_path.is_file():
        review = pd.read_csv(review_path, keep_default_na=False)
        if len(review) != EXPECTED_ROWS:
            raise RuntimeError(
                f"Existing review CSV has {len(review)} rows; expected {EXPECTED_ROWS}"
            )

        for col in [
            "row_index",
            "relative_path",
            "category",
            "corrected_garment_id",
            "corrected_fold_id",
            "clean_image_relative_path",
            "clean_png_sha256",
        ]:
            if col not in review.columns:
                raise RuntimeError(f"Existing review CSV missing required column: {col}")
            if review[col].astype(str).tolist() != base[col].astype(str).tolist():
                raise RuntimeError(f"Existing review CSV authoritative column changed: {col}")

        for col, default in [
            ("target_text_status", ""),
            ("other_text_visible", False),
            ("review_note", ""),
        ]:
            if col not in review.columns:
                review[col] = default

        bad = sorted(
            {
                x
                for x in review["target_text_status"].astype(str)
                if x and x not in VALID_STATUSES
            }
        )
        if bad:
            raise RuntimeError(f"Invalid existing target_text_status values: {bad}")

        return review

    base["target_text_status"] = ""
    base["other_text_visible"] = False
    base["review_note"] = ""
    review_path.parent.mkdir(parents=True, exist_ok=True)
    base.to_csv(review_path, index=False, lineterminator="\n")
    return base


def write_review(review: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    review.to_csv(path, index=False, lineterminator="\n")


def bool_series(series: pd.Series) -> pd.Series:
    if series.dtype == bool:
        return series
    return series.astype(str).str.lower().isin({"true", "1", "yes"})


def finalize_review(
    authoritative_path: Path,
    review_path: Path,
    summary_path: Path,
    review: pd.DataFrame,
) -> None:
    statuses = review["target_text_status"].astype(str)
    incomplete = int((statuses == "").sum())
    if incomplete:
        raise RuntimeError(
            f"Cannot finalize target-text audit: {incomplete} rows remain unreviewed."
        )

    invalid = sorted(set(statuses) - VALID_STATUSES)
    if invalid:
        raise RuntimeError(f"Invalid target-text statuses: {invalid}")

    counts = statuses.value_counts().reindex(sorted(VALID_STATUSES), fill_value=0)
    target_positive_mask = statuses.isin(
        {"EXACT", "PARTIAL_OR_ABBREVIATED", "AMBIGUOUS"}
    )
    affected = review.loc[target_positive_mask].copy()

    summary = {
        "schema_version": 1,
        "experiment": "CLO-SKET Experiment 06 corrective reanalysis",
        "stage": "POST_OUTCOME_TARGET_TEXT_LEAKAGE_AUDIT_COMPLETE",
        "population_reviewed": int(len(review)),
        "review_status_counts": {k: int(v) for k, v in counts.items()},
        "target_identifying_or_ambiguous_rows": int(target_positive_mask.sum()),
        "target_identifying_or_ambiguous_fraction": float(target_positive_mask.mean()),
        "affected_categories": sorted(affected["category"].astype(str).unique().tolist()),
        "affected_category_count": int(affected["category"].nunique()),
        "affected_corrected_identities": int(affected["corrected_garment_id"].nunique()),
        "affected_folds": sorted(
            affected["corrected_fold_id"].astype(int).unique().tolist()
        ),
        "other_text_visible_rows": int(bool_series(review["other_text_visible"]).sum()),
        "target_text_leakage_cleared": bool(target_positive_mask.sum() == 0),
        "decision_rule": (
            "CLEARED only if EXACT=0, PARTIAL_OR_ABBREVIATED=0, and AMBIGUOUS=0 "
            "across all 2,300 frozen CLEAN images."
        ),
        "annotation_status_sha256": sha256_file(authoritative_path),
        "review_csv_sha256": sha256_file(review_path),
        "classifier_fitted": False,
        "prediction_computed": False,
        "predictive_metric_computed": False,
        "clean_images_modified": False,
    }

    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("Target-text leakage audit finalization: COMPLETE")
    print(f"Rows reviewed: {len(review)}")
    for status in sorted(VALID_STATUSES):
        print(f"{status}: {int(counts[status])}")
    print(
        "Target identifying or ambiguous rows: "
        f"{int(target_positive_mask.sum())}"
    )
    print(f"Target-text leakage cleared: {summary['target_text_leakage_cleared']}")
    print(f"Review CSV: {review_path}")
    print(f"Summary JSON: {summary_path}")
    print("No classifier, prediction, or predictive metric was computed.")


class ReviewApp:
    def __init__(
        self,
        root: tk.Tk,
        review: pd.DataFrame,
        clean_root: Path,
        review_path: Path,
    ) -> None:
        self.root = root
        self.review = review
        self.clean_root = clean_root
        self.review_path = review_path
        self.photo: ImageTk.PhotoImage | None = None

        incomplete = self.review.index[
            self.review["target_text_status"].astype(str) == ""
        ].tolist()
        self.index = incomplete[0] if incomplete else EXPECTED_ROWS - 1

        root.title("CLO-SKET Target-Text Leakage Audit")
        root.geometry("920x900")

        self.header = tk.Label(root, font=("Helvetica", 18, "bold"))
        self.header.pack(pady=(12, 4))

        self.subheader = tk.Label(root, font=("Helvetica", 13))
        self.subheader.pack(pady=(0, 8))

        self.image_label = tk.Label(root, bg="white", bd=2, relief="solid")
        self.image_label.pack(pady=8)

        self.status_label = tk.Label(root, font=("Helvetica", 13, "bold"))
        self.status_label.pack(pady=6)

        self.other_label = tk.Label(root, font=("Helvetica", 12))
        self.other_label.pack(pady=4)

        help_text = (
            "Space/N = NONE   E = EXACT   P = PARTIAL/ABBREVIATED   "
            "A = AMBIGUOUS\nO = toggle other text   B = back   Q = save & quit"
        )
        self.help = tk.Label(root, text=help_text, font=("Helvetica", 12))
        self.help.pack(pady=8)

        self.progress = tk.Label(root, font=("Helvetica", 12))
        self.progress.pack(pady=4)

        root.bind("<space>", lambda event: self.set_status("NONE"))
        root.bind("n", lambda event: self.set_status("NONE"))
        root.bind("e", lambda event: self.set_status("EXACT"))
        root.bind("p", lambda event: self.set_status("PARTIAL_OR_ABBREVIATED"))
        root.bind("a", lambda event: self.set_status("AMBIGUOUS"))
        root.bind("o", lambda event: self.toggle_other())
        root.bind("b", lambda event: self.go_back())
        root.bind("q", lambda event: self.quit())
        root.protocol("WM_DELETE_WINDOW", self.quit)

        self.render()

    def current_row(self):
        return self.review.iloc[self.index]

    def render(self) -> None:
        row = self.current_row()
        image_path = self.clean_root / row["clean_image_relative_path"]

        with Image.open(image_path) as image:
            image.load()
            display = image.convert("L").resize((672, 672), Image.Resampling.NEAREST)

        self.photo = ImageTk.PhotoImage(display)
        self.image_label.configure(image=self.photo)

        self.header.configure(
            text=f"TRUE CATEGORY (outside image): {row['category']}"
        )
        self.subheader.configure(
            text=(
                f"Row {int(row['row_index'])}   |   "
                f"{row['relative_path']}   |   "
                f"Fold {int(row['corrected_fold_id'])}"
            )
        )

        status = str(row["target_text_status"]) or "UNREVIEWED"
        self.status_label.configure(text=f"Target-text status: {status}")

        other = bool_series(pd.Series([row["other_text_visible"]])).iloc[0]
        self.other_label.configure(text=f"Other non-target text visible: {bool(other)}")

        completed = int(
            (self.review["target_text_status"].astype(str) != "").sum()
        )
        self.progress.configure(
            text=f"Reviewed {completed}/{EXPECTED_ROWS}   |   Current row {self.index + 1}/{EXPECTED_ROWS}"
        )

    def set_status(self, status: str) -> None:
        if status not in VALID_STATUSES:
            raise RuntimeError(status)

        self.review.at[self.index, "target_text_status"] = status
        write_review(self.review, self.review_path)

        if self.index < EXPECTED_ROWS - 1:
            self.index += 1
            self.render()
        else:
            remaining = int(
                (self.review["target_text_status"].astype(str) == "").sum()
            )
            write_review(self.review, self.review_path)
            if remaining == 0:
                messagebox.showinfo(
                    "Review complete",
                    "All 2,300 rows are reviewed. Quit and run --finalize.",
                )
            else:
                first = self.review.index[
                    self.review["target_text_status"].astype(str) == ""
                ][0]
                self.index = int(first)
                self.render()

    def toggle_other(self) -> None:
        current = bool_series(
            pd.Series([self.review.at[self.index, "other_text_visible"]])
        ).iloc[0]
        self.review.at[self.index, "other_text_visible"] = not bool(current)
        write_review(self.review, self.review_path)
        self.render()

    def go_back(self) -> None:
        if self.index > 0:
            self.index -= 1
            self.render()

    def quit(self) -> None:
        write_review(self.review, self.review_path)
        self.root.destroy()


def main() -> None:
    args = parse_args()

    clean_root = args.clean_root.expanduser().resolve()
    annotation_status = args.annotation_status.expanduser().resolve()
    review_path = args.review_csv.expanduser().resolve()
    summary_path = args.summary_json.expanduser().resolve()

    if not clean_root.is_dir():
        raise RuntimeError(f"Clean root does not exist: {clean_root}")
    if not annotation_status.is_file():
        raise RuntimeError(f"Annotation status does not exist: {annotation_status}")

    authoritative = load_authoritative_status(annotation_status, clean_root)

    if args.verify_only:
        print("VERIFY-ONLY COMPLETE — no review labels or predictive outcomes computed.")
        return

    review = initialize_or_load_review(authoritative, review_path)

    if args.finalize:
        finalize_review(
            annotation_status,
            review_path,
            summary_path,
            review,
        )
        return

    print("Opening human target-text review GUI...")
    print("No classifier, prediction, or predictive metric will be computed.")

    root = tk.Tk()
    ReviewApp(root, review, clean_root, review_path)
    root.mainloop()


if __name__ == "__main__":
    main()
