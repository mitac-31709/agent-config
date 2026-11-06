# Pinned upstream catalogs

These directories are git submodules. Each one is a pointer to one commit of an upstream repository. This repository does not copy those trees into its own files.

The authoritative pin is the gitlink (`mode 160000`) stored in git. The SHAs below match those gitlinks. A pin does not move when upstream adds commits. Moving it means checking out a new commit and committing the new gitlink.

## Checkout

Direct pins only (does not fetch nested submodules, and does not run upstream installers):

```bash
git clone https://github.com/mitac-31709/agent-config.git
cd agent-config
git submodule update --init
```

`git clone --recurse-submodules` also checks out the direct pins. It then walks nested submodules. Today the only nested set is inside `google/skills`: 16 Google Cloud data plugins declared in that repo's own `.gitmodules`. Those nested repos are not separate pins of this repository.

An existing clone that was created without submodules:

```bash
git submodule update --init
```

Add `--recursive` only when you also want the nested Google Cloud plugins.

## What the pin means

`.gitmodules` records the HTTPS upstream URL and the path. It does not record a branch. The commit that is checked out is the gitlink in the parent commit.

To look at upstream without moving the pin:

```bash
git -C external/catalogs/<owner>/<repo> fetch origin
git -C external/catalogs/<owner>/<repo> rev-parse HEAD origin/HEAD
```

To move one pin on purpose, fetch upstream, check out the commit you want, then commit the gitlink in this repository:

```bash
git -C external/catalogs/<owner>/<repo> fetch origin
git -C external/catalogs/<owner>/<repo> checkout <commit>
git add external/catalogs/<owner>/<repo>
git commit
```

`git submodule update --remote <path>` checks out the upstream default branch tip because `.gitmodules` sets no branch. That changes the working checkout only. The pin other people get stays the old gitlink until that change is committed.

## These checkouts are not already enabled

Putting a catalog here does not register it with Codex, Claude Code, Cursor, GitHub Copilot, Gemini, or any other product. This repo's own skill directory is `.agents/skills/`, and the only skill there is `pick-tools-from-stars`. Codex looks for `.agents/skills` from the working directory upward. It does not treat `external/catalogs/` as that directory.

Upstream install paths differ, and this repository does not run them:

- Several catalogs document `npx skills add <owner>/<repo>` (Google, Microsoft, Vercel, Cloudflare).
- Claude Code catalogs document marketplace commands such as `/plugin marketplace add` and `/plugin install`.
- Codex plugin catalogs document their own plugin or marketplace install, or a manual copy into `.agents/skills` (Hugging Face documents the copy/symlink).
- Cursor plugins are installed through Cursor's plugin flow. Cloudflare also documents Cursor Marketplace or a remote rule.
- GitHub Copilot's awesome-copilot collection documents `copilot plugin install`.

Copying one skill folder into the path that product actually scans is a separate, explicit step. Do not run upstream hooks, package scripts, or installers just because the submodule is present. Some upstream trees contain those scripts.

## Inventory

Pins below were the default-branch tips on 2026-11-06, compared with `git ls-remote <url> HEAD`. Licenses were read from the GitHub license API and upstream README or LICENSE files. Where those disagree, both are stated. Upstream licenses stay with the upstream commits. This repository's own `LICENSE` remains MIT and does not relicense them.

| Path | Upstream | License | Why it is pinned |
|------|----------|---------|------------------|
| `agentskills/agentskills` | https://github.com/agentskills/agentskills.git | Apache-2.0 | Specification repo for the Agent Skills format cited as https://agentskills.io. `83021e2be457a9b6679148719c1f6074f0ad975e` |
| `anthropics/skills` | https://github.com/anthropics/skills.git | No repo-level license file. Upstream says many skills are Apache-2.0 and that the document skills are source-available. Each skill has its own `LICENSE.txt` | Anthropic skill examples named by `pick-tools-from-stars` and `references/index.md`. `ca45fc496a3436251f191354091d557da31c15b5` |
| `anthropics/claude-plugins-official` | https://github.com/anthropics/claude-plugins-official.git | Apache-2.0 | Official Claude Code plugin directory named by the skill and the URL index. Not the same tree as `anthropics/skills`. `1aa4a4b10e6c5e8694d0f72a03dbac4e93bcafd8` |
| `openai/plugins` | https://github.com/openai/plugins.git | No repo-level license. Some plugin directories include their own LICENSE file | Current Codex plugin examples. The skill names this repo. `b767f8fa3be1a22b093127dd59956c91ecffca9d` |
| `cursor/plugins` | https://github.com/cursor/plugins.git | Root README says MIT. GitHub did not detect a root LICENSE file | Official Cursor plugins named by the skill. `2776ddd2355d6d6c8747d3964600f28daf62f049` |
| `github/awesome-copilot` | https://github.com/github/awesome-copilot.git | MIT | GitHub organization's community catalog of Copilot agents, instructions, and skills, named by the skill. `96543145e9cb97711020b57b9d88f968062c4fc7` |
| `google/skills` | https://github.com/google/skills.git | Apache-2.0 | Google product skills named by the skill. Nested Cloud plugin repos stay in upstream `.gitmodules` and are not duplicated here. `c2cf4ba74c0e47f0e7a81d29e053e740998a0ae2` |
| `vercel-labs/agent-skills` | https://github.com/vercel-labs/agent-skills.git | Root README says MIT. GitHub did not detect a root LICENSE file | Vercel agent skills named by the skill and the URL index. `1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62` |
| `huggingface/skills` | https://github.com/huggingface/skills.git | Apache-2.0 | Hugging Face skills named by the skill and the URL index. `25910b3d0ba31a2ba102f901cdc9e008c278a69c` |
| `microsoft/skills` | https://github.com/microsoft/skills.git | MIT | Microsoft / Azure / Foundry skills named by the skill. Upstream marks the repo as still in progress. `4f831bbbf54e004507758d8ef2ab420c77bb81b6` |
| `cloudflare/skills` | https://github.com/cloudflare/skills.git | Apache-2.0 | Cloudflare skills named by the skill. `1f2cd0a19588e2c6197c91dd7c71729df1fb6156` |

## Not pinned

- `openai/skills` is named by the skill and by `references/index.md`, and it is still a public repo, but its README says it is deprecated and points people to `openai/plugins`. Pinning both would duplicate the stale tree.
- https://agentskills.io and the Codex cloud docs are websites, not git repositories. The specification git repo is pinned; the website is not.
- `openai/codex` is the product repository. The URL index only cites one issue, so the product tree is not pinned.
- `google-gemini/skills` and `awslabs/agent-skills` do not exist (GitHub 404). The skill names those orgs only as examples for `npx skills find --owner`.
- The 16 nested Google Cloud plugin repositories are upstream submodules of `google/skills`, not additional direct pins.
- Personal star snapshots and private agent data are not part of this tree.
