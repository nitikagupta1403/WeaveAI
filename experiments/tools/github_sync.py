from pathlib import Path
import shutil
import subprocess
import os

def sync_experiment(experiment, token):

    drive_figs = Path(
        f"/content/drive/MyDrive/WeaveAI/experiments/{experiment}/figures"
    )

    repo_figs = Path(
        f"/content/WeaveAI/experiments/{experiment}/figures"
    )

    repo_figs.mkdir(parents=True, exist_ok=True)

    copied = 0

    for png in drive_figs.glob("*.png"):
        shutil.copy2(png, repo_figs / png.name)
        print("✓", png.name)
        copied += 1

    print(f"\nCopied {copied} figure(s)\n")

    os.chdir("/content/WeaveAI")

    subprocess.run(
        ["git","add",f"experiments/{experiment}"]
    )

    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            f"Update figures for {experiment}"
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

    subprocess.run(
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

    print("\n━━━━━━━━━━━━━━━━━━━━━━")
    print(" GitHub Sync Complete")
    print("━━━━━━━━━━━━━━━━━━━━━━")
    print("Experiment :", experiment)
    print("Figures    :", copied)
