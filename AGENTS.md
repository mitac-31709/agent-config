# Agent notes

## Skills

This repo ships agent skills under `.agents/skills/`. If a skill below isn't in your skill list, open its `SKILL.md` and follow it anyway.

- `pick-tools-from-stars` (`.agents/skills/pick-tools-from-stars/SKILL.md`): use it whenever you need to choose a tool, library, CLI, MCP server, or agent skill. It searches the user's GitHub stars and official skill catalogs, then recommends maintained options.

## Rules

`rules/work-preferences.md` records the owner's work preferences. They are preferences only. They do not override product safety rules, and they do not override an explicit instruction in the current task.

## References

See `references/index.md` for public skill-format and catalog URLs. The index is not a complete catalog and does not include third-party skill text.

## External catalogs

`external/catalogs/` is a set of pinned upstream checkouts. They are not skills of this repo, and being checked out does not enable them in a product. Do not run their installers, hooks, or package scripts unless the current task explicitly asks for that. Details and the license list are in `external/catalogs/README.md`.

## Scope

`MANIFEST.md` lists what this public repository contains. It is an initial shareable set, not a full export of any agent.
