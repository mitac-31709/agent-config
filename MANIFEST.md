# Manifest

Public inventory of what this repository currently contains.

This is an initial collection of shareable material. It is not a complete export of any agent, bot, memory store, or private workspace.

## Published here

| Path | What it is |
|------|------------|
| `.agents/skills/pick-tools-from-stars/` | User-authored skill, MIT. Personal star snapshots are not included. |
| `rules/work-preferences.md` | Owner work preferences. Preferences only. They do not override safety rules or an explicit instruction for the current task. |
| `references/index.md` | URLs of public docs and vendor catalogs. No third-party skill text copied into this repo. |
| `external/catalogs/` | Gitlinks to upstream catalogs. Not copies of those trees, and not enabled in any product merely by being present. |
| `LICENSE` | MIT for this repository. Upstream catalogs keep their own licenses. |

The submodule inventory, URLs, license notes, pins, clone commands, and non-goals are in [`external/catalogs/README.md`](external/catalogs/README.md). Summary:

| Path | Upstream | License as checked | Purpose |
|------|----------|--------------------|---------|
| `external/catalogs/agentskills/agentskills` | https://github.com/agentskills/agentskills | Apache-2.0 | Agent Skills specification |
| `external/catalogs/anthropics/skills` | https://github.com/anthropics/skills | Per-skill; many Apache-2.0, document skills source-available | Anthropic skill examples |
| `external/catalogs/anthropics/claude-plugins-official` | https://github.com/anthropics/claude-plugins-official | Apache-2.0 | Official Claude Code plugins |
| `external/catalogs/openai/plugins` | https://github.com/openai/plugins | No repo-level license; some paths have one | Current Codex plugin examples |
| `external/catalogs/cursor/plugins` | https://github.com/cursor/plugins | README says MIT; no root LICENSE file detected | Official Cursor plugins |
| `external/catalogs/github/awesome-copilot` | https://github.com/github/awesome-copilot | MIT | GitHub Copilot community catalog |
| `external/catalogs/google/skills` | https://github.com/google/skills | Apache-2.0 | Google product skills |
| `external/catalogs/vercel-labs/agent-skills` | https://github.com/vercel-labs/agent-skills | README says MIT; no root LICENSE file detected | Vercel agent skills |
| `external/catalogs/huggingface/skills` | https://github.com/huggingface/skills | Apache-2.0 | Hugging Face skills |
| `external/catalogs/microsoft/skills` | https://github.com/microsoft/skills | MIT | Microsoft / Azure skills |
| `external/catalogs/cloudflare/skills` | https://github.com/cloudflare/skills | Apache-2.0 | Cloudflare skills |

## Not published here

- Personal GitHub star snapshots
- Third-party skill text copied into this repository's own files
- Credentials, private notes, and conversation logs

Generated star snapshots stay local. `.gitignore` excludes `references/stars*` and `**/references/stars*`.
