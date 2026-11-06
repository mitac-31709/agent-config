# agent-config

Public home for shareable agent skills, work preferences, and reference links.

Skills use the open [Agent Skills](https://agentskills.io) format (`SKILL.md`) and can be used with Codex, Claude Code, Cursor, and other agents that read `.agents/skills/`.

This repository is an initial public collection. It is not a full export of any agent, bot, or private workspace. See [MANIFEST.md](MANIFEST.md).

## Layout

| Path | Contents |
|------|----------|
| `.agents/skills/` | Reusable agent skills |
| `rules/` | Owner work preferences (not system prompts, and not safety policy) |
| `references/` | Index of public docs and catalogs (URLs only) |
| `external/catalogs/` | Pinned upstream catalog checkouts (gitlinks, not copied files) |

## Skills

### `pick-tools-from-stars`

When a task needs a tool, library, CLI, MCP server, or agent skill, the agent:

1. clarifies the need and constraints (OS, GPU, license, offline, ...),
2. searches **your GitHub stars** (a local snapshot if you made one, otherwise live via `gh api`),
3. searches **official skill catalogs** (`npx skills find`, vendor repos such as `openai/skills`, `anthropics/skills`),
4. filters by quality (stars, last push, archived, license),
5. recommends one top pick plus 2-3 alternatives, with reasons and sources.

It is read-only by default: installing or starring anything requires your OK.

## Install into a repo

Copy the skill folder into the repo where you run your agent:

```bash
git clone https://github.com/mitac-31709/agent-config /tmp/agent-config
mkdir -p .agents/skills
cp -r /tmp/agent-config/.agents/skills/pick-tools-from-stars .agents/skills/
```

The earlier repository name `agent-skills` redirects here. This copy step only needs the skill in this repository. It does not initialize `external/catalogs/`.

For local Codex you can instead put the skill in `~/.agents/skills/` to use it in every repo.

### Optional: bundle a snapshot of your stars

Without a snapshot the skill fetches your stars live (needs network and `gh`). To make it work offline or faster:

```bash
python3 .agents/skills/pick-tools-from-stars/scripts/refresh_stars.py <your-github-login>
```

This writes `references/stars.csv` and `references/stars_by_list.md` inside the skill folder (star-list names are included when `gh` is logged in as that user). The data is personal; `.gitignore` excludes it. Commit it only to a private repo.

## Rules and references

- [`rules/work-preferences.md`](rules/work-preferences.md) — how the owner prefers agents to work. Preferences only.
- [`references/index.md`](references/index.md) — public documentation and catalog URLs. No third-party skill text copied into this repo.

## Upstream catalogs

[`external/catalogs/`](external/catalogs/README.md) pins official skill and plugin catalogs that this repo already cites. Each entry is a submodule: an HTTPS URL plus a gitlink to one commit. The upstream files are not copied into this repository.

A checkout of this repo does not enable those catalogs in Codex, Claude Code, Cursor, Copilot, or any other product. `.agents/skills/` still contains only `pick-tools-from-stars`. See `external/catalogs/README.md` for the inventory, licenses, init commands, and the separate install step each product documents.

Direct pins only:

```bash
git clone https://github.com/mitac-31709/agent-config.git
cd agent-config
git submodule update --init
```

`git clone --recurse-submodules` also fetches nested submodules declared by those upstream repos. Today that means the Google Cloud plugins inside `google/skills`. Neither command runs upstream installers. An existing clone uses `git submodule update --init`.

The committed gitlink is a fixed commit. Upstream moving its default branch does not move this pin. Updating means checking out a new commit and committing the new gitlink.

## Codex cloud note

Codex documents that skills stored in the selected repository are available in cloud tasks ([cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments)). Automatic discovery of those repository skills is still reported as missing ([openai/codex#52266](https://github.com/openai/codex/issues/52266)). If the skill is not offered automatically, invoke it explicitly:

```
$pick-tools-from-stars find a good tool for ...
```

or say "read `.agents/skills/pick-tools-from-stars/SKILL.md` and follow it". `AGENTS.md` points to the skill as an extra fallback.

## License

[MIT](LICENSE)
