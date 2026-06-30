"""Git operations: check repo, get staged diff, commit."""
import subprocess


def is_git_repo() -> bool:
    """Return True if current directory is inside a git repository."""
    try:
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            capture_output=True,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_staged_diff() -> str:
    """Return staged diff. Raise ValueError if no changes staged."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--no-color"],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to get git diff: {e.stderr.strip()}") from e

    diff = result.stdout.strip()
    if not diff:
        raise ValueError(
            "No staged changes found. Use `git add` to stage files first."
        )
    return diff


def commit(message: str) -> None:
    """Execute git commit with the given message."""
    try:
        subprocess.run(
            ["git", "commit", "-m", message],
            check=True,
            capture_output=True,
            text=True,
        )
        print("Commit successful.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Git commit failed: {e.stderr.strip()}") from e


__all__ = ["is_git_repo", "get_staged_diff", "commit"]
