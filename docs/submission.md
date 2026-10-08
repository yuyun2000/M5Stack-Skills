# Public plugin submission handoff

The prepared publisher is **yuyun2000**. Package name: `m5stack-skills`.
Display name: **M5Stack Skills**. Initial version: **0.1.0**.
The repository is the single maintained source for all four skills.

## Prepared materials

- Portable `plugin.json` and public SSE `mcp.json` configuration.
- Four complete MIT skill packages, bundled upstream notices and source hashes.
- Original circuit icon, with a 256px PNG and editable SVG source.
- Public [privacy notice](../PRIVACY.md) and [package terms](../TERMS.md).
- Reproducible plugin ZIP, four skill ZIPs and SHA-256 checksums on GitHub Releases.
- Community announcements and demo recording scripts in [launch-kit.md](launch-kit.md).

The SVG/PNG is an original package icon, not the M5Stack corporate logo.
Do not claim a completed video walkthrough or device test from the recording scripts.

## Portal steps requiring publisher access

Follow the current [OpenAI submission guide](https://developers.openai.com/plugins/deploy/submission):

1. Sign in to the publisher's OpenAI organization/project and complete personal
   developer identity verification. A GitHub login does not establish this.
2. Upload `m5stack-skills-0.1.0.zip`, including its MCP configuration from the start.
3. Select the package's public MCP and complete the portal's domain-verification
   challenge. `mcp.m5stack.com` is operated by M5Stack; coordinate the exact
   challenge with that operator rather than claiming personal domain control.
4. Resolve metadata, skill and MCP scan findings; run and record the actual
   review cases. Attach a real walkthrough URL if required by the portal.
5. Submit for review. After approval, publish and verify the public listing URL.

No token, registered-app ID, verification status or approval result is invented
in this repository. The plugin schema checks are not a portal review result.
The delivery session could not access browser UI because browser control timed
out; upload, review and publication remain pending.

## Positive review cases

These are prepared test cases. Only package installation, firmware catalog and
MCP search smoke tests were run; model behavior cases below need execution in a
fresh installed-plugin session before submission.

| Case | Prompt | Expected evidence |
| --- | --- | --- |
| UIFlow2 code | Generate a CoreS3 ENV III temperature/humidity display. | Reads the matching bundled API docs; checks firmware/wiring; emits code and validation steps without inventing a device PASS. |
| UI improvement | Improve a supplied 320 x 240 UIFlow2 sensor dashboard. | Uses the coder/designer pair; chooses a documented rendering system and distinguishes static from visual/device checks. |
| Public firmware | Find current Cardputer ADV firmware candidates. | Queries public M5Burner data; preserves the variant, IDs and versions; includes date and prerequisites. |
| Product support | Check CoreS3 Grove pins using official information. | Calls `knowledge_search` with product filtering and cites returned evidence. |
| Troubleshooting | Explain a supplied sanitized UIFlow2 import error for an exact firmware. | Distinguishes missing firmware capability from code/API mistakes; uses official sources or marks uncertainty. |

## Negative review cases

- Do not claim firmware compatibility from popularity or a similarly named device.
- Do not submit feedback containing Wi-Fi passwords or customer data.
- Do not flash hardware or upload firmware in response to a discovery request.
- If the MCP is unavailable, report failure and use the documented official-source fallback.
- Without device/visual evidence, do not mark code or UI as hardware/visual PASS.

## ClawHub

The [ClawHub license rules](https://docs.openclaw.ai/clawhub/skill-format#license)
require MIT-0 and do not allow per-skill license overrides. The current packages
retain upstream MIT materials. Publication would require a separately authorized,
compatible package; changing the existing license or deleting notices is not
part of this delivery.
