# agent-skills

Agent skills in the open [Agent Skills](https://agentskills.io) format (`SKILL.md`), usable with Codex, Claude Code, Cursor, and other agents that read `.agents/skills/`.

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
git clone https://github.com/mitac-31709/agent-skills /tmp/agent-skills
mkdir -p .agents/skills
cp -r /tmp/agent-skills/.agents/skills/pick-tools-from-stars .agents/skills/
```

For local Codex you can instead put it in `~/.agents/skills/` to use it in every repo.

### Optional: bundle a snapshot of your stars
Without a snapshot the skill fetches your stars live (needs network and `gh`). To make it work offline or faster:

```bash
python3 .agents/skills/pick-tools-from-stars/scripts/refresh_stars.py <your-github-login>
```

This writes `references/stars.csv` and `references/stars_by_list.md` (star-list names are included when `gh` is logged in as that user). The data is personal; `.gitignore` excludes it here. Commit it only to a private repo.

## Codex cloud: current workaround
Codex cloud is documented to load skills from the selected repo's `.agents/skills/`, but repo skills currently aren't auto-discovered in cloud tasks ([openai/codex#52266](https://github.com/openai/codex/issues/52266)). Until that's fixed, invoke the skill explicitly in your prompt:

```
$pick-tools-from-stars find a good tool for ...
```

or say "read `.agents/skills/pick-tools-from-stars/SKILL.md` and follow it". `AGENTS.md` here points to the skill as an extra fallback.

## License
[MIT](LICENSE)
