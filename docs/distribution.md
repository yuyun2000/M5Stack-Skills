# Distribution and discovery

Publisher: **yuyun2000**, personal developer identity. Rules and observed status
below were checked on **2026-10-08**.

## Install from GitHub through the skills CLI

```bash
npx skills add yuyun2000/M5Stack-Skills
npx skills add yuyun2000/M5Stack-Skills --skill uiflow2-coder uiflow2-ui-designer
```

Use `--list` to preview available skills without installing. The four packages
were discovered and installed with skills CLI **1.7.1** into an isolated Codex
project. All **401 files** matched the repository by SHA-256; executable script
modes and the designer's sibling-document links were verified. No user-wide
agent installation was changed.

The default symlink installation of the coder/designer pair was also tested in
an isolated Claude Code project. Both entry points and cross-skill references
resolved successfully; this verifies installation, not model execution.

## Directory status

| Channel | Action / observable status |
| --- | --- |
| skills.sh | A real CLI installation of all four packages completed. The [FAQ](https://www.skills.sh/docs/faq) says public install telemetry powers directory discovery. The initial page check did not establish an exact matching catalog entry; listing remains unconfirmed. |
| SkillsMP | Added the required `claude-skills` and `claude-code-skill` GitHub topics. Its [FAQ](https://skillsmp.com/docs/faq) describes automatic GitHub indexing and says manual submission is not yet available. The initial creator/repository page probe returned 404; indexing remains unconfirmed. |
| ChatGPT / Codex public directory | Portable plugin ZIP and submission materials prepared. Public approval/publication has not occurred. Verified personal publisher identity, portal access and MCP domain verification are required. |
| M5Stack community | English/Chinese announcement and three demonstration scripts prepared. Posting requires an authenticated community session; no forum post has been sent. |
| ClawHub | Original MIT packages have not been published. The [platform format rules](https://docs.openclaw.ai/clawhub/skill-format#license) require MIT-0 with no per-skill overrides. Do not remove or replace bundled upstream MIT notices to satisfy this rule. |

The directory page probes are limited observations, not proof that a crawler has
finished or that a listing has been rejected. No installation counts or stars
are claimed. A real installation test is not a substitute for organic adoption.

## Downloadable artifacts

[GitHub Releases](https://github.com/yuyun2000/M5Stack-Skills/releases) provide:

- `m5stack-skills-0.1.0.zip`: portable plugin with all four skills, public SSE
  MCP configuration, PNG/SVG icon, policy documents and original license notices.
- One `skill-name-0.1.0.zip` per skill, each with one top-level skill folder.
- `SHA256SUMS.txt`: archive checksums.
- `m5stack-launch-kit-0.1.0.zip`: community announcements, demo recording scripts
  and shareable SVG/PNG workflow cards.

The source is maintained once under `skills/`; no second editable skill copy is
created for plugin distribution. Rebuild from the repository root:

```bash
python3 scripts/build_distribution.py --output-dir /tmp/m5stack-skills-release
```

Choose a new empty output directory. The builder refuses existing archive files,
uses fixed ZIP metadata, preserves executable bits and verifies every archive
member against the source. CI builds and verifies the same artifacts.

## Plugin installation and submission

`plugin.json` follows the portable Agent Plugins format. `mcp.json` declares the
public `https://mcp.m5stack.com/sse` server with the `sse` transport.
The package has no hooks, credentials or registered-app IDs.

The repository includes a Codex marketplace catalog under
`.agents/plugins/marketplace.json`. Users who choose to add this source can run:

```bash
codex plugin marketplace add yuyun2000/M5Stack-Skills --ref main
```

Then inspect and install the plugin through the desktop Plugins UI. This is a
repository marketplace source, separate from public directory approval. The
desktop installation flow has not been exercised in this delivery.

See [submission.md](submission.md) for publisher-facing portal steps and test
cases. Follow the [official plugin package guide](https://developers.openai.com/plugins/build/plugins)
and [submission guide](https://developers.openai.com/plugins/deploy/submission)
when submitting. Keep the MCP server in the initial submission: the current
guide does not support adding one to an already-created skills-only plugin.

## Promotion

Use [launch-kit.md](launch-kit.md) for publish-ready community text and recording
scripts. Promote the public repository, complete-package installation, official
documentation grounding and actual runtime evidence. Add fresh target-device
footage before making hardware or visual-success claims.
