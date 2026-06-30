"""Command-line interface for git-pulse."""
import sys
import argparse

from .git_ops import is_git_repo, get_staged_diff, commit
from .ai_client import get_client
from .hook import install_hook


def generate_message(
    diff: str,
    provider: str,
    model: str = None,
    api_url: str = None,
    api_key: str = None,
) -> str:
    """Call the AI provider and return a sanitized commit title."""
    client = get_client(provider, model, api_url, api_key)
    raw_msg = client.generate(diff)
    lines = raw_msg.splitlines()
    title = lines[0].strip() if lines else raw_msg.strip()
    # Remove markdown decorations and quotes
    title = title.strip("`").strip('"').strip("'")
    # Truncate to 72 characters
    if len(title) > 72:
        title = title[:72].rstrip()
    return title


def generate_command(args: argparse.Namespace) -> None:
    """Handle the 'generate' subcommand (default)."""
    if not is_git_repo():
        print("Error: Not inside a git repository.", file=sys.stderr)
        sys.exit(1)

    try:
        diff = get_staged_diff()
    except ValueError as e:
        if getattr(args, "hook", False):
            # Silent exit for hook mode when nothing is staged
            sys.exit(0)
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        message = generate_message(
            diff, args.provider, args.model, args.api_url, args.api_key
        )
    except Exception as e:
        print(f"Error generating commit message: {e}", file=sys.stderr)
        sys.exit(1)

    # If output file specified (hook mode), write and exit
    if args.output:
        try:
            with open(args.output, "w") as f:
                f.write(message + "\n")
        except IOError as e:
            print(f"Error writing to {args.output}: {e}", file=sys.stderr)
            sys.exit(1)
        sys.exit(0)

    # Interactive or automatic commit
    print(f"\nGenerated commit message:\n  {message}\n")
    if args.auto:
        try:
            commit(message)
        except RuntimeError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        while True:
            choice = input(
                "Do you want to proceed? (y)es / (e)dit / (a)bort: "
            ).strip().lower()
            if choice in ("y", "yes"):
                try:
                    commit(message)
                except RuntimeError as e:
                    print(f"Error: {e}", file=sys.stderr)
                    sys.exit(1)
                break
            elif choice in ("e", "edit"):
                new_msg = input("Enter your commit message: ").strip()
                if new_msg:
                    message = new_msg
                    if len(message) > 72:
                        message = message[:72].rstrip()
                    print(f"Updated message: {message}")
                else:
                    print("Empty message, aborting.")
                    sys.exit(0)
            elif choice in ("a", "abort"):
                print("Aborted.")
                sys.exit(0)
            else:
                print("Invalid choice. Please choose y, e, or a.")


def main():
    """Entry point for git-pulse CLI."""
    parser = argparse.ArgumentParser(
        description="git-pulse: AI conventional commit message generator"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"gitpulse {__import__('gitpulse').__version__}",
    )
    subparsers = parser.add_subparsers(dest="command")

    # generate subcommand (also used as default)
    gen_parser = subparsers.add_parser(
        "generate", help="Generate a commit message (default)"
    )
    gen_parser.add_argument(
        "--auto",
        action="store_true",
        help="Automatically commit without confirmation",
    )
    gen_parser.add_argument(
        "--output", help="Write message to file (for hook usage)"
    )
    gen_parser.add_argument(
        "--provider",
        default="opencode",
        help="AI provider (opencode, openai, ollama)",
    )
    gen_parser.add_argument("--model", help="Model name")
    gen_parser.add_argument("--api-url", help="API base URL")
    gen_parser.add_argument("--api-key", help="API key")
    gen_parser.add_argument(
        "--hook", action="store_true", help=argparse.SUPPRESS
    )

    # init subcommand
    subparsers.add_parser(
        "init", help="Install git-pulse as a pre-commit hook"
    )

    # If no subcommand is given, default to 'generate'
    args, unknown = parser.parse_known_args()
    if args.command is None:
        args = gen_parser.parse_args(unknown)
        generate_command(args)
    elif args.command == "generate":
        generate_command(args)
    elif args.command == "init":
        install_hook()


if __name__ == "__main__":
    main()
