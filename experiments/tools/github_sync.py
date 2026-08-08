from pathlib import Path
import shutil
import subprocess
import os

# Files we automatically synchronize
SYNC_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".pdf",
    ".csv",
    ".txt",
    ".md",
    ".ipynb",
    ".npy",
    ".npz",
    ".json"
}


def sync_experiment(experiment):
    """
    Synchronize an experiment from Google Drive to GitHub.

    Parameters
    ----------
    experiment : str
        Example:
        EXP-002-GradCAM-Sketch-Representation
    """

    token = os.environ.get("GITHUB_TOKEN")

    if token is None:
        raise RuntimeError(
            "GITHUB_TOKEN not found. Run the authentication cell first."
        )

    drive_root = Path(
        f"/content/drive/MyDrive/WeaveAI/experiments/{experiment}"
    )

    repo_root = Path(
        f"/content/WeaveAI/experiments/{experiment}"
    )

    repo_root.mkdir(parents=True, exist_ok=True)

    copied = []

    for file in drive_root.rglob("*"):

        if file.is_dir():
            continue

        if file.suffix.lower() not in SYNC_EXTENSIONS:
            continue

        relative = file.relative_to(drive_root)

        destination = repo_root / relative

        destination.parent.mkdir(parents=True, exist_ok=True)

        shutil.copy2(file, destination)

        copied.append(relative)

    os.chdir("/content/WeaveAI")

    subprocess.run(["git", "add", f"experiments/{experiment}"])

    commit = subprocess.run(
        [
            "git",
            "commit",
            "-m",
            f"Update {experiment}"
        ]
    )

    subprocess.run(
        [
            "git",
            "pull",
            "--rebase",
            "origin",
            "main"
        ]
    )

    subprocess.run(
        [
            "git",
            "remote",
            "set-url",
            "origin",
            f"https://{token}@github.com/nitikagupta1403/WeaveAI.git"
        ]
    )

    push = subprocess.run(
        [
            "git",
            "push",
            "origin",
            "main"
        ]
    )

    subprocess.run(
        [
            "git",
            "remote",
            "set-url",
            "origin",
            "https://github.com/nitikagupta1403/WeaveAI.git"
        ]
    )

    print("\n" + "=" * 60)
    print("        WeaveAI Experiment Sync")
    print("=" * 60)
    print(f"Experiment : {experiment}")
    print()

    print("Files synchronized:")

    if copied:
        for f in copied:
            print(f"   ✓ {f}")
    else:
        print("   (No supported files found)")

    print()

    print(f"Files copied : {len(copied)}")

    if commit.returncode == 0:
        print("Commit       : ✓")
    else:
        print("Commit       : No new changes")

    if push.returncode == 0:
        print("Push         : ✓")
    else:
        print("Push         : Failed")

    print("=" * 60)
