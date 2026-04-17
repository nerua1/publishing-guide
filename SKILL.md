---
name: publishing-guide
description: >
  Centralne zasady publikacji skilli na GitHub (nerua1) i ClawHub.
  Konwencja nazewnictwa, anti-duplicate rule, procedura publikacji,
  checklista pre-publish, status wszystkich publicznych repo.
  Używaj przed każdą publikacją nowego skilla.
version: "1.0.0"
author: "nerua1"
license: "MIT"
compatible-with: claude-code, openclaw, hermes-agent
tags: [publishing, github, clawhub, skills, guidelines, nerua1]
---

# Publishing Guide 📦

Centralne zasady publikacji skilli AI pod kontem **github.com/nerua1**.

---

## 1. Konwencja nazewnictwa

Każdy skill MUSI mieć **opisowy sufiks**:

| Sufiks | Kiedy używać | Przykład |
|--------|-------------|----------|
| `-loop` | Iteracyjna poprawa / feedback loop | `ralph-wiggum-loop` |
| `-bridge` | Komunikacja między agentami/systemami | `openclaw-bridge`, `acp-bridge` |
| `-stack` | Architektura / stack technologiczny | `shared-memory-stack` |
| `-guide` | Dokumentacja / setup / onboarding | `openclaw-setup-guide` |
| `-guard` | Bezpieczeństwo / audyt / weryfikacja | `safe-skill-install` |
| `-agent` | Autonomiczny agent / proactive | `proactive-agent` |
| `-crawler` | Scraping / crawling / fetching | `news-crawler` |
| `-skill` | Ogólny skill (gdy nic innego nie pasuje) | `god-mode-skill` |
| `-monitor` | Monitoring / healthcheck / observability | `lm-studio-monitor` |
| `-orchestrator` | Orkiestracja modeli / dispatch | `lm-studio-orchestrator` |

### Prefixy agent-specific
- Skill specyficzny dla **OpenClaw** → prefix `openclaw-`
- Skill specyficzny dla **Claude Code** → prefix `claude-` (rzadko, bo Claude vault jest domyślny)
- Skill **uniwersalny** → bez prefixu

### Zakazane nazwy
- Same imiona bez sufiksu (`ralph`, `hermes`) — za mało opisowe
- Sufiksy `-v1`, `-v2` w nazwie repo — wersjonowanie przez git tags
- CamelCase — używaj kebab-case

---

## 2. Anti-duplicate rule (MUSI być wykonana przed publikacją)

Przed każdym `git push` nowego publicznego repo:

```bash
# 1. GitHub
gh repo list nerua1 --limit 100 | grep -i "nazwa-skilla"

# 2. ClawHub
npx clawhub search nazwa-skilla

# 3. Lokalnie (OpenClaw workspace)
ls ~/.openclaw/workspace/skills/ | grep -i "nazwa-skilla"

# 4. Lokalnie (Claude vault)
ls ~/.claude/skills/vault/ | grep -i "nazwa-skilla"

# 5. Hermes skills
ls ~/.hermes/skills/ | grep -i "nazwa-skilla"
```

**Jeśli coś podobnego istnieje → nie publikuj.** Zaproponuj:
- Scalenie funkcjonalności do istniejącego skilla, lub
- Dodanie jako podkatalog/scripts do istniejącego repo

**Lesson learned:** `ralph` i `ralph-wiggum-loop` były osobnymi repo robiącymi podobne rzeczy → zmarnowany czas na scalanie.

---

## 3. Procedura publikacji

### Wymagania wstępne
- SSH key `~/.ssh/github_nerua1` dodany do GitHub
- `gh` authenticated as `nerua1`
- `git config --global user.name nerua1`
- `git config --global user.email neru_a1@icloud.com`

### Claude Code skills (`~/.claude/skills/vault/`)

```bash
SKILL_NAME="moj-nowy-skill"
cd ~/.claude/skills/vault/${SKILL_NAME}

# Sprawdź czy SKILL.md ma poprawny frontmatter
head -5 SKILL.md

# Inicjalizuj repo
git init
git add .
git commit -m "feat: ${SKILL_NAME} v1.0.0"

# Utwórz publiczne repo i wyślij
gh repo create ${SKILL_NAME} --public --source . --remote origin --push
```

### OpenClaw skills (`~/.openclaw/workspace/skills/`)

```bash
# Metoda 1: przez ClawHub (preferowana)
/publish-skill moj-nowy-skill

# Metoda 2: ręcznie (gdy ClawHub nie działa)
cd ~/.openclaw/workspace/skills/moj-nowy-skill
git init && git add . && git commit -m "feat: moj-nowy-skill v1.0.0"
gh repo create moj-nowy-skill --public --source . --remote origin --push
```

### Hermes skills (`~/.hermes/skills/`)

Hermes NIE ma własnego registry — skille Hermesa publikuj jako OpenClaw skills lub Claude vault skills z tagiem `compatible-with: hermes-agent`.

---

## 4. Checklista pre-publish

- [ ] Nazwa zgodna z konwencją (sufiks + ewentualny prefix)
- [ ] Anti-duplicate check wykonany (GitHub + ClawHub + lokalnie)
- [ ] `SKILL.md` zawiera YAML frontmatter z `name`, `description`, `version`, `author`, `license`
- [ ] `SKILL.md` ma sekcję `## Install` i `## Usage`
- [ ] Brak hardcoded secrets / API keys
- [ ] Brak plików `.env` w repo
- [ ] `.gitignore` zawiera: `node_modules/`, `.env`, `*.log`, `.DS_Store`
- [ ] README.md (dla GitHub) lub SKILL.md (dla ClawHub) jest kompletne
- [ ] Testowane lokalnie przed push
- [ ] Wersja zaczyna się od `1.0.0` (SemVer)
- [ ] Tag `compatible-with` zawiera wszystkich agentów na których działa

---

## 5. Publiczne repozytoria — status

| Repo | Typ | Opis | Ostatni update |
|------|-----|------|----------------|
| `nerua1/openclaw-bridge` | vault | Claude Code ↔ OpenClaw messaging | 2026-04-12 |
| `nerua1/shared-memory-stack` | vault | Memory architecture reference | 2026-04-12 |
| `nerua1/ralph` | vault | Persistence loop do skutku | 2026-04-12 |
| `nerua1/ralph-wiggum-loop` | vault | Generator→Critic→Fixer→Verifier | 2026-04-12 |
| `nerua1/openclaw-setup-guide` | vault | M4 setup guide, RAM reality, pitfalls | 2026-04-12 |
| `nerua1/god-mode-skill` | skill | Prompt engineering / safety bypass | 2026-04-13 |
| `nerua1/arena-council-skill` | skill | Multi-model council + voting | 2026-04-13 |
| `nerua1/skill-vetter` | tool | Security audit przed instalacją | 2026-04-12 |
| `nerua1/skill-install-pipeline` | tool | Secure install pipeline | 2026-04-12 |
| `nerua1/nerua1` | meta | Meta-repo ze wszystkimi skillami | 2026-04-13 |

### Lokalne (nieopublikowane lub WIP)

| Skill | Lokalizacja | Status |
|-------|-------------|--------|
| `lm-studio-orchestrator` | `~/.claude/skills/vault/` | Ready to publish |
| `system-bridge` | `~/.claude/skills/vault/` | Ready to publish |
| `acp-bridge` | `~/.openclaw/skills/` | WIP |
| `kimi-bridge` | `~/.openclaw/skills/` | Private (API keys) |

---

## 6. Szybkie komendy

```bash
# Lista Twoich publicznych repo
gh repo list nerua1 --limit 100

# Stworzenie nowego skilla (template)
mkdir ~/.claude/skills/vault/nowy-skill-name
# skopiuj SKILL.md z istniejącego skilla jako template

# Aktualizacja REGISTRY.md po publikacji
# EDYTUJ: ~/.claude/skills/REGISTRY.md
```

---

## 7. Kontakt / Wsparcie

- GitHub: https://github.com/nerua1
- ClawHub: `npx clawhub search nerua1`
- PayPal (jeśli komuś się przydało): https://paypal.me/nerudek
