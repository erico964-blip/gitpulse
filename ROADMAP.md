# Roadmap

## v0.2.0 (Planned)

- [ ] Support Azure OpenAI
- [ ] Support Anthropic Claude
- [ ] Configurable commit templates (e.g., `{type}: {description}` vs `{type}({scope}): {description}`)
- [ ] Multiple language support for commit messages
- [ ] `git-pulse --dry-run` to preview without committing

## v0.3.0 (Future)

- [ ] GitHub Actions integration (auto-generate PR commit messages)
- [ ] VS Code extension
- [ ] Caching for repeated diffs
- [ ] Interactive diff review (show what changed before generating)
- [ ] Support for `gitmoji` alongside Conventional Commits

## Ideas & Backlog

- [ ] Web dashboard to review generated messages
- [ ] Team commit message style enforcement
- [ ] `pre-commit` hook integration (besides native git hook)
- [ ] Custom system prompt via config file
- [ ] Shell completions (bash, zsh, fish, powershell)
