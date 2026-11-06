# Official references (URL index)

Public documentation and catalogs useful for agent skills and tooling. This file lists URLs only. It does not copy third-party skill bodies into this repository.

Pinned checkouts of the git repositories live under `external/catalogs/` as submodules. See that directory's README for licenses, commit pins, and why a checkout is not the same as enabling a product.

The list is not exhaustive. Entries below are ones this repo already cites, checked as public pages or vendor repositories on 2026-11-06. Confirm a repository is still owned by that vendor before treating it as official.

## Skill format

- Agent Skills site: https://agentskills.io
- Specification repository (pinned): https://github.com/agentskills/agentskills

## Vendor skill and plugin catalogs

Pinned as submodules unless noted:

- OpenAI plugins (current Codex examples, pinned): https://github.com/openai/plugins
- OpenAI skills: https://github.com/openai/skills — still cited by `pick-tools-from-stars`, but upstream marks this repository deprecated and points to `openai/plugins`. Not pinned.
- Anthropic skills (pinned): https://github.com/anthropics/skills
- Anthropic Claude plugins (pinned): https://github.com/anthropics/claude-plugins-official
- Cursor plugins (pinned): https://github.com/cursor/plugins
- GitHub awesome-copilot (pinned): https://github.com/github/awesome-copilot
- Google skills (pinned): https://github.com/google/skills
- Vercel Labs agent-skills (pinned): https://github.com/vercel-labs/agent-skills
- Hugging Face skills (pinned): https://github.com/huggingface/skills
- Microsoft skills (pinned): https://github.com/microsoft/skills
- Cloudflare skills (pinned): https://github.com/cloudflare/skills

## Related docs and issues

- Codex cloud environments (docs say repository skills are available in cloud tasks): https://learn.chatgpt.com/docs/environments/cloud-environments
- Report that repository skills are missing from automatic discovery in Codex cloud: https://github.com/openai/codex/issues/52266

## This repository

- https://github.com/mitac-31709/agent-config

> Discovery command used by the skill: `npx -y skills find "<query>"` (optional `--owner <publisher>`). Requires network.
