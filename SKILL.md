---
name: publishing-guide
description: Central publishing rules for nerudek repos — naming convention, anti-duplicate, checklist, full inventory of all 25 public repos. Use before every skill publication.
version: "1.2.0"
author: nerudek
license: MIT
compatible-with: claude-code, openclaw, hermes-agent
---
# Publishing Guide

## 1. Naming Convention
- Suffix: -skill for standalone tools (god-mode-skill), no suffix for vault/libraries
- Prefix: skill- for wrapper skills (skill-cancel, skill-note etc)
- NEVER duplicate: check GitHub + ClawHub before creating

## 2. Anti-duplicate Rule
- Search GitHub: gh search repos --owner nerudek NAZWA
- Search ClawHub: npx clawhub search NAZWA
- Search local: ls ~/.hermes/skills ~/.openclaw/workspace/skills

## 3. Pre-publish Checklist
- [ ] SKILL.md with YAML frontmatter (name, description, version, author, license)
- [ ] No hardcoded secrets/API keys
- [ ] .gitignore: node_modules/, .env, *.log
- [ ] compatible-with lists all supported agents
- [ ] PayPal footer at bottom
- [ ] Tested locally

## 4. Public Repositories (25 total)

| Repo | Type | Status |
|------|------|--------|
| acp-bridge | vault | active |
| arena-council-skill | skill | active |
| god-mode-skill | skill | active |
| hermes-agent | skill | active |
| multi-agent-harness | vault | active |
| nerudek | profile | active |
| nerudek-platform | platform | active |
| openclaw | vault | active |
| openclaw-bridge | vault | active |
| openclaw-setup-guide | vault | active |
| publishing-guide | meta | active |
| ralph-wiggum-loop | skill | active |
| shared-memory-stack | vault | active |
| skill-acp-bridge | skill | DEPRECATED (merged) |
| skill-cancel | skill | OpenClaw-only |
| skill-github-promotion | skill | active |
| skill-install-pipeline | tool | OpenClaw-only |
| skill-nerudek-workspace | vault | active |
| skill-note | skill | OpenClaw-only |
| skill-ralph | skill | DEPRECATED |
| skill-ram-negotiation | skill | active |
| skill-ultrawork | skill | OpenClaw-only |
| skill-vetter | tool | OpenClaw-only |
| vibe-safe | skill | active |
| vibe-safe-starter | skill | active |

## 5. Publishing Commands
```bash
# GitHub
gh repo create SKILL_NAME --public --source . --push

# ClawHub
npx clawhub publish
```

## 6. Hermes Skills
Hermes skills live in ~/.hermes/skills/. Add compatible-with: hermes-agent.

---

If this saved you time: [support me](https://www.paypal.me/nerudek)
