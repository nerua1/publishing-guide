# nerudek Public Repository Inventory (updated 2026-05-10)

25 public repos on github.com/nerudek

| # | Repo | Type | Status |
|---|------|------|--------|
| 1 | acp-bridge | vault | active — ACP inter-agent communication |
| 2 | arena-council-skill | skill | active — multi-model voting council |
| 3 | god-mode-skill | skill | active — prompt engineering (ULTRAPLINIAN→Ultra-Plinian fixed) |
| 4 | hermes-agent | skill | active — Hermes agent docs |
| 5 | multi-agent-harness | vault | active — HARNESS.md, paths fixed |
| 6 | nerudek | profile | active — SKILL.md added 2026-05-07 |
| 7 | nerudek-platform | platform | active |
| 8 | openclaw | vault | active |
| 9 | openclaw-bridge | vault | OpenClaw-only — compatible-with: openclaw |
| 10 | openclaw-setup-guide | vault | active |
| 11 | publishing-guide | meta | active — v2.1.0, SKILL.hermes.md files tracked |
| 12 | ralph-wiggum-loop | skill | active — Generator→Critic→Fixer→Verifier |
| 13 | shared-memory-stack | vault | active — hermes-agent added to compatible-with |
| 14 | skill-acp-bridge | skill | DEPRECATED — merged into acp-bridge |
| 15 | skill-cancel | skill | HERMES — SKILL.hermes.md added (hermes-agent native) |
| 16 | skill-github-promotion | skill | active — copy-paste bug fixed |
| 17 | skill-install-pipeline | tool | HERMES — SKILL.hermes.md added (no ClawHub dependency) |
| 18 | skill-nerudek-workspace | vault | active |
| 19 | skill-note | skill | HERMES — SKILL.hermes.md added (memory() tool native) |
| 20 | skill-ralph | skill | DEPRECATED — use ralph-wiggum-loop |
| 21 | skill-ram-negotiation | skill | active |
| 22 | skill-ultrawork | skill | HERMES — SKILL.hermes.md added (delegate_task native) |
| 23 | skill-vetter | tool | HERMES — SKILL.hermes.md added (search_files native) |
| 24 | vibe-safe | skill | active — quick-start/ added from starter |
| 25 | vibe-safe-starter | skill | active — merged into vibe-safe/quick-start |

## Hermes-Native Skills (2026-05-10 update)

These repos now have SKILL.hermes.md with `compatible-with: hermes-agent` using Hermes-native tools:

| Repo | Hermes-Native Tools Used |
|------|-------------------------|
| skill-vetter | search_files, read_file, terminal |
| skill-cancel | process(action='kill'), process(action='list'), terminal |
| skill-ralph | delegate_task, todo, memory, terminal, search_files |
| skill-ultrawork | delegate_task(tasks=[]), terminal(background=True) |
| skill-install-pipeline | git clone, search_files, read_file, write_file, skills_list |
| skill-note | memory(action='add'/'replace'/'remove') |

Key changes from OpenClaw versions:
- No `openclaw` CLI commands
- No `npx clawhub` dependency
- No `openclaw sessions spawn` → replaced with `delegate_task`
- No file-based state (`~/.openclaw/state/`) → replaced with `memory()` and `todo()`
- No shell scripts (`cancel.sh`, `note.sh`) → replaced with native tool calls
