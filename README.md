# ⚡ Git Pulse

> **AI-powered conventional commit messages, right from your terminal.**

[![PyPI version](https://badge.fury.io/py/gitpulse.svg)](https://badge.fury.io/py/gitpulse)
[![PyPI downloads](https://img.shields.io/pypi/dm/gitpulse.svg)](https://pypi.org/project/gitpulse/)
[![GitHub stars](https://img.shields.io/github/stars/erico964-blip/gitpulse?style=social)](https://github.com/erico964-blip/gitpulse/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python versions](https://img.shields.io/pypi/pyversions/gitpulse.svg)](https://pypi.org/project/gitpulse/)

![Demo GIF placeholder](https://via.placeholder.com/800x400?text=Git+Pulse+Demo)

Stop struggling with commit messages. **Git Pulse** reads your staged changes, asks your favorite AI model, and generates a perfect [Conventional Commit](https://www.conventionalcommits.org/) message – ready to use.

---

## ✨ Features

- 🧠 Uses AI to understand your code diff and craft meaningful messages
- 📐 Strict Conventional Commits format (`feat(scope): description`)
- 🔒 Title never exceeds 72 characters
- 🎮 Interactive (confirm/edit/abort) or fully automatic mode
- 🪝 One-command hook installation (`git pulse init`)
- 🔌 Pluggable providers: **OpenCode**, **OpenAI**, **Ollama** (more soon)
- 🐍 Tiny dependency: only `requests` – Python 3.8+

---

## 🚀 Quickstart

### 1. Install

```bash
pip install gitpulse
```

### 2. Configure your AI provider

By default, Git Pulse uses **OpenCode** (local or remote). Set the environment variables:

```bash
export OPENCODE_API_URL="http://localhost:8080/v1/chat/completions"
export OPENCODE_API_KEY="your-key-here"
```

If you prefer **OpenAI**:

```bash
export OPENAI_API_KEY="sk-..."
```

Or **Ollama**:

```bash
export OLLAMA_API_URL="http://localhost:11434/api/generate"
```

### 3. Make some changes and stage them

```bash
git add .
```

### 4. Let Git Pulse generate your commit message

```bash
git pulse
```

You'll see a generated message like `feat(auth): add JWT token validation`.
Confirm, edit, or abort – it's that simple.

For fully automated pipelines:

```bash
git pulse --auto
```

---

## 📦 Usage

```
git pulse [options]                  # generate a commit message
git pulse init                       # install the prepare-commit-msg hook
```

### Options for `git pulse`

| Flag | Description |
|------|-------------|
| `--auto` | Automatically commit without confirmation |
| `--provider` | AI provider: `opencode` (default), `openai`, `ollama` |
| `--model` | Model name (e.g., `gpt-4o-mini`) |
| `--api-url` | Override API base URL |
| `--api-key` | Override API key |
| `--output` | Write message to a file (used internally by the hook) |

### Git Hook

After running `git pulse init`, every time you run `git commit`, the hook will:

1. Check for staged changes
2. Generate a conventional commit message automatically
3. Open your editor with the message pre-filled (or commit directly if `--auto` was set).

---

## 🔧 Supported AI Providers

| Provider | Default Model | Env Vars |
|----------|--------------|----------|
| **OpenCode** | `opencode` | `OPENCODE_API_URL`, `OPENCODE_API_KEY` |
| **OpenAI** | `gpt-4o-mini` | `OPENAI_API_KEY` |
| **Ollama** | `llama3` | `OLLAMA_API_URL` |

You can pass `--provider`, `--model`, `--api-url`, and `--api-key` at runtime to override defaults.

---

## 🤖 How It Works

1. Extracts the `git diff --cached` output
2. Sends it together with a carefully engineered system prompt to the AI endpoint
3. Parses the response, strips any formatting, truncates to 72 characters
4. If in interactive mode, lets you review and edit; if automatic, commits immediately

The system prompt is designed to produce only the commit message, nothing else.

---

## 🛠 Development

Clone the repo and install in editable mode:

```bash
git clone https://github.com/erico964-blip/gitpulse
cd gitpulse
pip install -e .
```

Run tests (coming soon):

```bash
pytest
```

---

## 📜 License

MIT © erico964-blip

---

⭐ **Star the repo** — If Git Pulse saves you from a few minutes of commit-message anguish, give it a star on GitHub!
