# Contributing to gitpulse

We love contributions! Here's how to get started.

## Development Setup

```bash
git clone https://github.com/erico964-blip/gitpulse
cd gitpulse
pip install -e ".[dev]"
```

## How to Contribute

1. **Fork** the repo
2. Create a branch: `git checkout -b feat/my-feature`
3. Make your changes and commit using `git-pulse` 😉
4. Push and open a **Pull Request**

## Running Tests

```bash
pytest
```

## Code Style

- Follow PEP 8 with type hints
- Keep commits in [Conventional Commits](https://www.conventionalcommits.org/) format
- Add docstrings for public functions
- Keep the 72-char limit for commit messages (the tool enforces this!)

## Reporting Issues

Open an issue on GitHub with:
- Steps to reproduce
- Expected vs actual behavior
- Environment details (`git-pulse --version`, OS, Python version)

## Adding a New AI Provider

1. Create a new class in `ai_client.py` extending `AIClient`
2. Implement the `generate(diff: str) -> str` method
3. Register it in the `get_client()` factory
4. Add default env vars in `config.py`
5. Update the README provider table

---

MIT © erico964-blip
