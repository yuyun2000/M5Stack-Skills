# M5Stack Skills

[English](README.md)

面向 M5Stack 产品支持、UIFlow2 MicroPython 编程、嵌入式界面设计和公开固件查询的
Agent Skill 仓库。每个 skill 都包含 `SKILL.md` 入口，以及使用时需要的文档、脚本或示例。

## 选择 skill

| Skill | 适用场景 | 依赖 |
| --- | --- | --- |
| [uiflow2-coder](skills/uiflow2-coder/SKILL.md) | 基于内置官方 API 文档编写、调试、审查 UIFlow2 MicroPython 代码。 | 查阅内置文档无需联网；可选搜索脚本需要 Bash 或 PowerShell。 |
| [uiflow2-ui-designer](skills/uiflow2-ui-designer/SKILL.md) | 设计、美化和优化屏幕、仪表盘、动画及嵌入式交互。 | 与 `uiflow2-coder` 并排安装，用其文档核对 API。 |
| [m5stack-firmware-query](skills/m5stack-firmware-query/SKILL.md) | 查询 M5Burner 公开固件、设备、版本、榜单和推荐候选。 | Python 3.10+，能访问 `https://burner.m5stack.com`，无需 API key。 |
| [m5stack-assistant](skills/m5stack-assistant/SKILL.md) | 查官方资料，回答规格、引脚、兼容性、开发和故障排查问题。 | M5Stack 公开 MCP；可选查询 CLI 需要 Node.js 18+。 |

UIFlow2 相关 skill 面向 UIFlow2 MicroPython。实际板卡能力、固件版本和 API 支持范围
仍需按目标设备核对。

## 安装

### 使用 skills CLI 安装

在需要使用 skill 的项目目录中运行：

```bash
npx skills add yuyun2000/M5Stack-Skills
```

按提示选择 Agent 和需要安装的 skill。UI 设计的两个 skill 建议一起安装：

```bash
npx skills add yuyun2000/M5Stack-Skills --skill uiflow2-coder uiflow2-ui-designer
```

[skills CLI](https://github.com/vercel-labs/skills)支持 Codex、Claude Code 等 Agent，
会安装完整包；MCP 仍需单独配置。标准 CLI 安装会参与
[skills.sh 目录统计](https://www.skills.sh/docs/faq)，可通过 `DISABLE_TELEMETRY=1`
关闭遥测。

### 手动安装

```bash
git clone https://github.com/yuyun2000/M5Stack-Skills.git
cd M5Stack-Skills
```

将所需 skill 的完整目录复制到 Agent 的技能目录。当前 Codex 的用户级目录为
`~/.agents/skills/`，项目级目录为目标项目内的 `.agents/skills/`，具体以
[官方安装说明](https://developers.openai.com/codex/skills)为准。仅克隆仓库不会自动安装。

下面的 macOS/Linux 示例安装四个 skill；发现已有同名目录或符号链接会停止。
更新已有版本前，先检查并备份旧目录。

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
    raise SystemExit('请先检查已有 skill：' + ', '.join(conflicts))
destination.mkdir(parents=True, exist_ok=True)
for name in names:
    shutil.copytree(source / name, destination / name)
print('已安装：' + ', '.join(names))
PY
```

`uiflow2-coder` 和 `uiflow2-ui-designer` 必须放在同一级目录。其他支持 Agent Skills
的工具请使用各自文档规定的目录，并保留完整包结构。若 Codex 未显示新 skill，
重启后再检查。安装 skill 不会自动配置 MCP。

## 配置 M5Stack MCP

使用 `m5stack-assistant` 时，在支持 MCP 的客户端中配置公开 SSE 地址：

```text
https://mcp.m5stack.com/sse
```

按客户端的远程 MCP/SSE 配置方式连接，并确认能看到 `knowledge_search`、
`knowledge_answer` 和 `knowledge_feedback`。内置 Node.js 查询 CLI 可直接连接，
但只封装 `knowledge_search`。查询和反馈会发到远端，请勿传入凭据、Wi-Fi 密码、
客户数据等敏感内容。

## 使用示例

安装后可直接向 Agent 提问：

```text
使用 $uiflow2-coder，为 CoreS3 编写读取 ENV III 并显示结果的 UIFlow2 程序。
使用 $uiflow2-ui-designer，优化 320 x 240 的 UIFlow2 传感器仪表盘。
使用 $m5stack-firmware-query，查询 Cardputer ADV 当前有哪些公开固件。
使用 $m5stack-assistant，依据官方资料核对 CoreS3 Grove 接口引脚。
```

也可在仓库根目录运行独立工具：

```bash
bash skills/uiflow2-coder/scripts/find_doc.sh env temperature
python3 skills/m5stack-firmware-query/scripts/m5stack_firmware_query.py devices --format table
node skills/m5stack-assistant/m5-search.mjs "CoreS3 引脚定义" --filter product
```

固件查询只读。使用这些 skill 不代表授权烧录、发布固件或改变设备状态。
生成代码和静态检查通过，也不代表已完成真机运行或视觉验收。

## 来源与维护

首批四个包于 **2026-10-08** 从 M5Stack Skill Hub 获取。
[skills-lock.json](skills-lock.json)记录源版本更新时间、归档和内容哈希、文件数及
公开版调整，不包含私有服务地址或 Hub 评论。内置文档是快照，请按目标固件核对。

官方来源：[UIFlow2 源仓库](https://github.com/m5stack/uiflow-micropython)、
[UIFlow2 API 文档](https://uiflow-micropython.readthedocs.io/en/latest/)、
[M5Stack 产品文档](https://docs.m5stack.com)。

维护与检查步骤见 [CONTRIBUTING.md](CONTRIBUTING.md)。问题反馈请提交
[GitHub Issue](https://github.com/yuyun2000/M5Stack-Skills/issues)，附上产品、固件版本、
复现步骤和已脱敏的错误输出。

## 插件与社区分发

仓库也提供 `m5stack-skills` 可移植插件清单及 M5Stack 公开 SSE MCP 配置。
完整插件 ZIP 和单个 skill ZIP 可从
[GitHub Releases](https://github.com/yuyun2000/M5Stack-Skills/releases)下载。
插件使用个人发布者身份 **yuyun2000**。

[分发说明](docs/distribution.md)包含打包检查、目录状态和公开插件市场的提交前提；
[推广材料](docs/launch-kit.md)包含中英文社区发布稿及三份演示录制脚本。
插件包准备完成与市场上架、真机演示录制是分别验证的步骤。

## 许可证

采用 [MIT 许可证](LICENSE)。请保留 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)
中说明的上游版权和许可信息。外部固件、服务及链接资源按各自许可证和条款使用。
