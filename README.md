# M5Stack Skills

[简体中文](README.zh-CN.md)

Reusable agent skills for M5Stack product support, UIFlow2 MicroPython development,
embedded interface design, and public firmware discovery. Each package contains
a `SKILL.md` entry point and the references, scripts, or examples it needs.

## Available skills

| Skill | Use it for | Dependencies |
| --- | --- | --- |
| [uiflow2-coder](skills/uiflow2-coder/SKILL.md) | Write, debug, and review UIFlow2 MicroPython using bundled official API documentation and curated examples. | No network needed to read the bundled docs; Bash or PowerShell for optional search helpers. |
| [uiflow2-ui-designer](skills/uiflow2-ui-designer/SKILL.md) | Design and improve M5Stack screens, dashboards, animations, and embedded interactions. | Install `uiflow2-coder` alongside it for API references. |
| [m5stack-firmware-query](skills/m5stack-firmware-query/SKILL.md) | Search public M5Burner firmware, devices, versions, rankings, and recommendations. | Python 3.10+ and access to `https://burner.m5stack.com`; no API key needed. |
| [m5stack-assistant](skills/m5stack-assistant/SKILL.md) | Answer product, pinout, compatibility, development, and troubleshooting questions from official sources. | M5Stack public MCP; Node.js 18+ for the optional search CLI. |

The UIFlow2 packages target UIFlow2 MicroPython. Hardware availability, firmware
versions, and board-specific APIs must still be checked for the target device.

## Install

Clone this repository:

```bash
git clone https://github.com/yuyun2000/M5Stack-Skills.git
cd M5Stack-Skills
```

Copy the complete skill folders into your agent's skill directory. For current
Codex, use `~/.agents/skills/` for user-wide installation or `.agents/skills/`
inside the target project. See the [official skill documentation](https://developers.openai.com/codex/skills).
Cloning into an arbitrary directory alone does not install the skills.

This macOS/Linux example installs all four and stops if a same-named folder or
symlink already exists. Review and back up existing installations before updating.

```bash
python3 - <<'PY'
from pathlib import Path
import shutil

source = Path('skills')
destination = Path.home() / '.agents' / 'skills'
names = ('uiflow2-coder', 'uiflow2-ui-designer',
         'm5stack-firmware-query', 'm5stack-assistant')
conflicts = [name for name in names
             if (destination / name).exists() or (destination / name).is_symlink()]
if conflicts:
    raise SystemExit('Review existing skills first: ' + ', '.join(conflicts))
destination.mkdir(parents=True, exist_ok=True)
for name in names:
    shutil.copytree(source / name, destination / name)
print('Installed: ' + ', '.join(names))
PY
```

Keep `uiflow2-coder` and `uiflow2-ui-designer` as sibling folders. For other agents,
use their documented skill directory and preserve the complete package structure.
If the skills do not appear in Codex, restart it. Installing a skill does not
automatically configure its MCP dependency.

## Configure M5Stack MCP

For `m5stack-assistant`, connect your MCP-capable client to the public SSE endpoint:

```text
https://mcp.m5stack.com/sse
```

Use the client's remote MCP/SSE configuration and confirm that
`knowledge_search`, `knowledge_answer`, and `knowledge_feedback` are available.
The included Node.js CLI connects directly and only calls `knowledge_search`.
Queries and feedback leave your machine; omit credentials, Wi-Fi passwords,
customer data, and other private content.

## Try it

Example prompts after installation:

```text
Use $uiflow2-coder to write a CoreS3 UIFlow2 program that displays ENV III readings.
Use $uiflow2-ui-designer to improve a 320 x 240 UIFlow2 sensor dashboard.
Use $m5stack-firmware-query to find current public firmware for Cardputer ADV.
Use $m5stack-assistant to check CoreS3 Grove pin definitions using official sources.
```

Standalone commands from this repository's root:

```bash
bash skills/uiflow2-coder/scripts/find_doc.sh env temperature
python3 skills/m5stack-firmware-query/scripts/m5stack_firmware_query.py devices --format table
node skills/m5stack-assistant/m5-search.mjs "CoreS3 pinout" --filter product
```

Firmware discovery is read-only. These skills do not authorize flashing,
publishing firmware, or changing device state. Generated code and static checks
are not proof of real-device execution or visual correctness.

## Sources and maintenance

The initial packages were retrieved from M5Stack Skill Hub on **2026-10-08**.
[skills-lock.json](skills-lock.json) records the source timestamps, archive and
content hashes, file counts, and public-package adjustments. It contains no
private service addresses or Hub comments. These are snapshots, not live docs.

UIFlow2 source and current documentation:
[m5stack/uiflow-micropython](https://github.com/m5stack/uiflow-micropython),
[UIFlow2 API docs](https://uiflow-micropython.readthedocs.io/en/latest/), and
[M5Stack product docs](https://docs.m5stack.com).

For checks and updates, see [CONTRIBUTING.md](CONTRIBUTING.md).
Report reproducible issues through [GitHub Issues](https://github.com/yuyun2000/M5Stack-Skills/issues).

## License

[MIT](LICENSE). Preserve the upstream copyright and license notices described
in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). External firmware, services,
and linked resources retain their respective licenses and terms.
