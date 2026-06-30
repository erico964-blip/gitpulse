# 📢 Promo Kit — gitpulse

Textos prontos para publicar nas comunidades.

---

## Reddit — r/git

**Title:** Tired of writing commit messages? I built a CLI that generates them for you

**Body:**

Every developer has a few `git commit -m "fix"` or `git commit -m "update"` in their history. I got fed up and built a tool that reads your staged diff and generates a proper Conventional Commit message — no thinking required.

```bash
pip install gitpulse-commit
git add src/utils.py
git-pulse
# → feat(utils): add email validation function
```

**What it does:**
- Reads `git diff --cached` and produces a Conventional Commit (≤72 chars)
- Interactive mode: you confirm, edit, or abort before committing
- `--auto` for pipelines
- `git-pulse init` installs it as a prepare-commit-msg hook — works on every commit

**How it generates messages:** By default it uses a local or remote AI endpoint (OpenCode, OpenAI-compatible, or Ollama). You control where your code goes — use Ollama locally if privacy matters. Under the hood it's a prompt that enforces the Conventional Commits spec: type, optional scope, imperative description, 72-char cap.

**Why I built it:** I juggle several side projects. Keeping clean commit histories across all of them was mental overhead I didn't need. Now I stage, run one command, confirm, and move on.

**Stack:** Python 3.8+, only `requests` as dependency. 7 modules, ABC + factory for pluggable providers. MIT license.

GitHub: https://github.com/erico964-blip/gitpulse
PyPI: https://pypi.org/project/gitpulse-commit/

Curious what you think — especially about the hook workflow.

---

## Dev.to — Artigo

**Title:** How I Built an AI-Powered Conventional Commit Generator in Python

**Tags:** `python` `git` `cli` `opensource` `ai`

**Body:**

```markdown
I shipped my first Python CLI to PyPI this week. Here's what I learned building **gitpulse** — a tool that reads your staged git diff and generates Conventional Commit messages using AI.

## The Problem

Every developer has lazy commits in their history:
`git commit -m "fix"`
`git commit -m "update"`
`git commit -m "stuff"`

Clean commit histories matter — for changelogs, code reviews, and your future self trying to understand why you changed that line 6 months ago. But writing `feat(auth): add JWT token validation with refresh support` for every single commit is mental overhead nobody needs.

## The Solution

gitpulse reads your staged diff and generates the message for you:

`pip install gitpulse-commit`
`git add src/auth.py`
`git-pulse`
`# → feat(auth): add JWT token validation`

You confirm, edit, or abort. One key. Done.

## What I Learned

### 1. PyPI packaging is simpler than it looks

`pyproject.toml` + `python -m build` + `twine upload` is all you need. No `setup.py`, no `setup.cfg`. The hardest part was finding an available package name (hint: check PyPI before you start coding).

### 2. ABC + factory pattern for pluggable providers

The core `AIClient` is abstract. Each provider (OpenCode, OpenAI, Ollama) implements `generate(diff) -> str`. The factory function just does `return OpenAIClient(...)` based on a string. Adding a new provider is ~20 lines of code.

### 3. Prompt engineering is API design

The system prompt is the most important file in the project. It enforces:
- Conventional Commits format (`type(scope): description`)
- 72-character max
- No markdown, no explanations, no fluff
- Imperative mood, no period at end

If the AI ignores any of these, the CLI still strips markdown and truncates — defense in depth.

### 4. Git hooks are easy but fragile

`git-pulse init` writes a prepare-commit-msg hook. It works great, but detecting an existing hook without breaking it required a sentinel marker (`## GITPULSE_HOOK_V0.1`) rather than just searching for a comment string.

### 5. GitHub Actions CI/CD is a superpower

```yaml
on:
  push:
    tags:
      - 'v*'
```

Now `git tag v0.2.0 && git push --tags` automatically publishes to PyPI. Zero manual steps.

## The Code

7 modules, ~300 lines of Python:
- `cli.py` — argparse with subcommands
- `ai_client.py` — ABC + 3 providers
- `git_ops.py` — subprocess wrappers
- `hook.py` — git hook installer
- `config.py` — env var getters
- `prompts.py` — the system prompt
- `__init__.py` — version

Only dependency: `requests`. Python 3.8+. MIT license.

## Try It

`pip install gitpulse-commit`

GitHub: [erico964-blip/gitpulse](https://github.com/erico964-blip/gitpulse)
PyPI: [gitpulse-commit](https://pypi.org/project/gitpulse-commit/)

Built this over a weekend. Feedback welcome — especially on the prompt design and hook workflow!
```

---

## Hacker News — Show HN

https://news.ycombinator.com/submit

**Title:** `Show HN: gitpulse — AI-generated conventional commits from your terminal`

**URL:** `https://github.com/erico964-blip/gitpulse`

**Text:** *(deixa vazio — Show HN com URL não tem campo de texto)*

**Depois de publicado, posta este comentário:**

```
Hi HN,

gitpulse reads your staged git diff and generates a Conventional Commit
message using AI (OpenCode, OpenAI, or local Ollama).

pip install gitpulse-commit
git add .
git-pulse
# → feat(auth): add JWT token validation

Interactive mode lets you confirm, edit, or abort. --auto for pipelines.
git-pulse init installs it as a prepare-commit-msg hook.

Tech: Python 3.8+, only requests as dependency. Pluggable providers
via ABC + factory. MIT license.

PyPI: https://pypi.org/project/gitpulse-commit/

Would love your feedback!
```

---

## Twitter / X

```
Just shipped gitpulse 🚀
AI generates your Conventional Commit messages from staged diffs.

pip install gitpulse-commit
github.com/erico964-blip/gitpulse
```

---

## LinkedIn

**Title:** I built a Python CLI that writes your git commit messages

**Body:**

Every developer has written `git commit -m "fix"` at least once. I built gitpulse to solve this.

It reads your staged diff, generates a Conventional Commit message (≤72 chars), and lets you confirm or edit before committing. Works offline with Ollama if privacy matters.

What I learned building this: PyPI packaging with `pyproject.toml`, ABC + factory pattern for pluggable AI providers, prompt engineering as API design, and GitHub Actions CI/CD.

```bash
pip install gitpulse-commit
```

GitHub: https://github.com/erico964-blip/gitpulse
PyPI: https://pypi.org/project/gitpulse-commit/

Open source, MIT license. Contributions welcome!

---

## Links para publicar

| Plataforma | Link |
|------------|------|
| **r/git** | https://www.reddit.com/r/git/submit |
| **Hacker News (Show HN)** | https://news.ycombinator.com/submit |
| **Dev.to** | https://dev.to/new |
| **LinkedIn** | https://www.linkedin.com/feed/ → "Start a post" |
| **Twitter/X** | https://x.com/ → Compose |
