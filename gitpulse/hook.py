"""Install git-pulse as a prepare-commit-msg hook."""
import os
import sys
import stat
import shutil
import subprocess


def install_hook() -> None:
    """Create or append the prepare-commit-msg hook."""
    try:
        git_root = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Not inside a git repository.", file=sys.stderr)
        sys.exit(1)

    hooks_dir = os.path.join(git_root, ".git", "hooks")
    hook_path = os.path.join(hooks_dir, "prepare-commit-msg")

    # Locate git-pulse executable
    git_pulse_cmd = shutil.which("git-pulse")
    if not git_pulse_cmd:
        git_pulse_cmd = "git-pulse"
        print(
            "Warning: 'git-pulse' not found in PATH. "
            "Make sure it's available when committing."
        )

    hook_script = f"""#!/bin/sh
## GITPULSE_HOOK_V0.1 — managed by `git pulse init`
# Git Pulse - AI conventional commit message generator
# This hook calls git-pulse to generate a commit message based on staged changes.
# If there are no staged changes, it skips.

if git diff --cached --quiet; then
    exit 0
fi

exec {git_pulse_cmd} --auto --output "$1"
"""
    if os.path.exists(hook_path):
        with open(hook_path, "r") as f:
            content = f.read()
        if "GITPULSE_HOOK" in content:
            print(
                "Git Pulse hook already installed. "
                "To update, remove the existing hook first."
            )
            return
        with open(hook_path, "a") as f:
            f.write("\n" + hook_script)
        print(f"Appended Git Pulse hook to existing {hook_path}")
    else:
        with open(hook_path, "w") as f:
            f.write(hook_script)
        os.chmod(hook_path, os.stat(hook_path).st_mode | stat.S_IEXEC)
        print(f"Created Git Pulse prepare-commit-msg hook at {hook_path}")

    print(
        "Hook installed successfully. "
        "Future commits will use AI-generated messages."
    )
