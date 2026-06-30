# 📢 Promo Kit — gitpulse

Textos prontos para publicar nas comunidades. Copia, cola, e ajusta se quiseres.

---

## Reddit — r/Python

**Title:** I built gitpulse — AI-powered conventional commits from your terminal

**Body:**

Hey r/Python! I got tired of staring at `git commit -m "fix stuff"` so I built a small CLI tool that reads your staged diff, sends it to an AI (OpenCode, OpenAI, or local Ollama), and generates a proper Conventional Commit message.

```bash
pip install gitpulse-commit
git add .
git-pulse
# → feat(utils): add email validation function
```

**Features:**
- Strict Conventional Commits format (≤72 chars)
- Interactive mode (confirm/edit/abort) or `--auto`
- One-command git hook: `git-pulse init`
- Pluggable AI providers: OpenCode, OpenAI, Ollama
- Only dependency is `requests` — Python 3.8+

**Links:**
- GitHub: https://github.com/erico964-blip/gitpulse
- PyPI: https://pypi.org/project/gitpulse-commit/

MIT license. Feedback welcome!

---

## Reddit — r/git

**Title:** Tired of writing commit messages? I built a tool that lets AI do it

**Body:**

`git-pulse` reads your staged diff and generates a Conventional Commit message using AI (local Ollama, OpenAI, or OpenCode).

```bash
pip install gitpulse-commit
git add some_file.py
git-pulse
```

It shows you the generated message — you can confirm, edit, or abort. Works with a git hook too (`git-pulse init` installs it as prepare-commit-msg).

GitHub: https://github.com/erico964-blip/gitpulse

Built this because I wanted clean commit histories without the mental overhead of writing good messages every time. Would love to hear what you think.

---

## Hacker News — Show HN

**Title:** Show HN: gitpulse — AI-generated conventional commits from your terminal

**Body:**

Hi HN,

I built gitpulse, a small Python CLI that generates Conventional Commit messages from your staged git diff using AI.

```bash
pip install gitpulse-commit
git add .
git-pulse
# → feat(auth): add JWT token validation
```

**How it works:**
1. Reads `git diff --cached`
2. Sends it to an AI endpoint with a system prompt that enforces the Conventional Commits spec
3. Returns a single line ≤72 characters — no fluff, no markdown

**Why:**
I run a lot of small experiments and side projects. Writing good commit messages for every single change became a bottleneck. Now I stage, run `git-pulse`, confirm, and move on. My commit history is cleaner than ever.

**Tech stack:**
- Python 3.8+, only `requests` as dependency
- Pluggable providers: OpenCode (default), OpenAI, Ollama (local)
- Git hook support (`git-pulse init`)
- MIT license

GitHub: https://github.com/erico964-blip/gitpulse
PyPI: `pip install gitpulse-commit`

Happy to answer questions!

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

**Title:** I built an AI tool that writes your git commit messages

**Body:**

Every developer has written `git commit -m "fix"` at least once. I built gitpulse to solve this.

It's a Python CLI that reads your staged diff, asks an AI model (OpenAI, Ollama, or OpenCode) to generate a Conventional Commit message, and lets you confirm or edit before committing.

**What I learned building this:**
- Packaging Python CLI tools for PyPI with `pyproject.toml` and `build`
- Designing a pluggable AI provider architecture (ABC + factory pattern)
- Enforcing strict output constraints (72-char Conventional Commits) through prompt engineering
- GitHub Actions CI/CD for automated PyPI publishing on version tags

**Try it:**
```bash
pip install gitpulse-commit
```

GitHub: https://github.com/erico964-blip/gitpulse
PyPI: https://pypi.org/project/gitpulse-commit/

Open source, MIT license. Contributions welcome!

---

## 📅 Timing Tips

- **Reddit:** Postar entre 9h-11h EST (14h-16h PT) nos dias de semana tem melhor alcance
- **Hacker News:** Os melhores dias são segunda-quarta, manhã (EST). Os posts duram ~24h na página Show
- **LinkedIn:** Terça/quarta/quinta ao meio-dia

## 🔗 Links Úteis

- GitHub: https://github.com/erico964-blip/gitpulse
- PyPI: https://pypi.org/project/gitpulse-commit/
- Reddit r/Python: https://www.reddit.com/r/Python/submit
- Reddit r/git: https://www.reddit.com/r/git/submit
- Hacker News Show HN: https://news.ycombinator.com/submit (começa o título com "Show HN: ")
