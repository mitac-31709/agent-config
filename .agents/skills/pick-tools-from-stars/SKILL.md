---
name: pick-tools-from-stars
description: >-
  Use this when choosing a tool, library, framework, CLI, MCP server, or agent
  skill for a task: first look in the user's own GitHub stars and in official
  vendor skill catalogs, then recommend well-known, actively maintained
  options with reasons.
---
# Pick tools from GitHub stars and official skill catalogs

Goal: when a task needs a tool, library, CLI, MCP server, or agent skill, prefer things the user already trusts (their GitHub stars) and official vendor catalogs over random web results, while still checking quality.

All paths below are relative to this skill's folder (the directory containing this SKILL.md).

## 1. Clarify the need
Write down in one line what the tool must do, plus hard constraints (language/runtime, OS, hardware such as GPU/VRAM, license, offline/local, budget). Use what you already know about the user's environment.

## 2. Search the user's GitHub stars
Find the user's GitHub login (ask once if unknown, or use `gh api user --jq .login` when `gh` is logged in as them). Then use the first source that exists:

1. **Local snapshot (optional).** If `references/stars.csv` or `references/stars_by_list.md` exists in this skill folder (or the user points you to a copy, e.g. in a separate private repo), search it first; it works offline.
   - `stars.csv` columns: `lists` (GitHub star list names, `|`-separated; `(unlisted)` if none), `full_name`, `url`, `description`, `description_ja`, `language`, `stars`, `pushed_at`, `archived`, `license`, `topics`, `starred_at`.
   - `stars_by_list.md`: the same repos grouped by star list, one line each, with a `Snapshot:` date at the top. List names are good category hints.
   - The snapshot can be stale; when online and freshness matters, also do the live check below.
2. **Live, read-only (default when no snapshot exists):**
   `gh api --paginate "users/<login>/starred?per_page=100" --jq '.[] | [.full_name,.html_url,.description,.language,(.topics|join(" ")),.stargazers_count,.pushed_at,.archived] | @tsv'`
   (or the unauthenticated REST API `https://api.github.com/users/<login>/starred` if `gh` is unavailable). If the user organizes stars into GitHub star lists, use the list names as category hints.

Match on description, topics, name, and language with several synonyms (including other languages the user writes in), e.g. `rg -i "video|動画|ffmpeg" references/stars.csv`. Skim the README of plausible hits before recommending.

## 3. Search official skill / plugin catalogs (when an agent skill or plugin would help)
- Run `npx -y skills find "<query>"`, optionally narrowed with `--owner <publisher>` to official publishers, e.g. anthropics, openai, cursor, github, google, google-gemini, microsoft, vercel-labs, cloudflare, huggingface, awslabs. This needs internet access; skip it and say so if the environment is offline.
- Also consider the vendors' official repos directly (e.g. anthropics/skills, anthropics/claude-plugins-official, openai/skills, openai/plugins, cursor/plugins, github/awesome-copilot, google/skills, vercel-labs/agent-skills, huggingface/skills, microsoft/skills, cloudflare/skills). Verify a repo is owned by the vendor's org before calling it official.

## 4. Quality filter (apply to every candidate)
- Use `stars`, `pushed_at`, `archived`, and `license` from the snapshot, and refresh them with `gh api repos/<owner>/<repo>` when online.
- Prefer well-known, actively maintained projects. Drop archived repos, ones with no meaningful activity in ~1 year, and ones with very few stars, unless nothing better exists (then say so).
- Stars can include old or joke repos: being starred is a signal of interest, not of quality.
- If nothing in the stars or official catalogs fits, say so and fall back to a normal search for the established standard tool. Never force a starred repo.

## 5. Recommend
- Give 1 top pick plus up to 2-3 alternatives. For each: name with link, one line on what it does, why it fits this task and constraints, stars and last update (say whether it came from the snapshot or a live check), and whether it came from the user's stars, an official catalog, or general search.
- Don't invent stars, dates, or features; only report what you verified.
- Installing, starring, or changing anything requires the user's go-ahead; this skill is read-only by default.

## Creating or updating a snapshot (optional)
`python3 scripts/refresh_stars.py <login>` writes `references/stars.csv` and `references/stars_by_list.md` (read-only; needs `gh` logged in; star-list names are filled in only when `gh` is logged in as `<login>`, otherwise every repo is `(unlisted)`). Existing `description_ja` values are kept. The data is personal: keep it out of public repos (see `.gitignore`) or store it in a separate private repo.
