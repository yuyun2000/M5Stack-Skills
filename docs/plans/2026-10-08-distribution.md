# Skill discovery and distribution

Publisher: `yuyun2000` (personal identity, confirmed by the user).

## Plan

- [x] Add a repository description and SkillsMP-compatible discovery topics.
- [x] Verify the skills CLI can discover and install all four complete packages
  in an isolated project; document the standard install command and UI skill pair.
- [x] Create a portable plugin package with public MCP configuration, publisher
  metadata, a local icon, and a reproducible ZIP builder.
- [x] Prepare English/Chinese community announcements and three demo scripts,
  using actual test evidence and no claims of hardware execution.
- [x] Validate manifests/package contents, installation, repository checks and CI;
  publish the GitHub changes and downloadable distribution artifacts.
- [x] Check public directory visibility; record observable status separately from
  indexing prerequisites. Attempt market/community publication if authenticated
  platform access is available.

Constraints: preserve the four source skill snapshots and MIT notices. Do not
relicense upstream material for ClawHub. Use personal publisher identity, not
company verification. Do not run hardware demos, submit MCP feedback or change
local/global agent installations while testing distribution.

Browser control timed out twice during initial session discovery. GitHub CLI
is available; platform login and submission cannot be inferred from that access.

## Evidence and remaining prerequisites

- Repository description and eight discovery topics were applied and read back.
- skills CLI 1.7.1 found all four packages. Copy-mode Codex installation matched
  401 source files and executable modes; default symlink-mode Claude Code
  installation of the UI pair preserved entry points and sibling references.
- Portable plugin/MCP manifests passed their published Agent Plugins schemas.
  Package ZIPs passed full source/member SHA-256 and local-link checks. Repeated
  builds produced identical checksums.
- Three SVG workflow cards were rendered to PNG and visually inspected. They
  show procedures, not device screenshots. English/Chinese announcements and
  three recording scripts are prepared.
- Initial skills.sh HTML did not establish an exact source/skill entry; the
  SkillsMP creator/repository page probe returned 404. Neither listing is claimed.
- Browser session discovery timed out twice. Community posting and OpenAI portal
  submission are pending usable login access, personal identity verification and
  coordination with the M5Stack MCP domain operator.
- ClawHub publication is pending a separately authorized license-compatible
  package. Existing upstream MIT material and notices remain unchanged.
- Distribution source commit: `fd75bd5`. Local/remote `main` matched, and
  [GitHub CI](https://github.com/yuyun2000/M5Stack-Skills/actions/runs/37745784417)
  passed, including offline tests and archive construction.
- [Release v0.1.0](https://github.com/yuyun2000/M5Stack-Skills/releases/tag/v0.1.0)
  is public with seven assets. Every downloaded asset matched its local source
  by SHA-256, and all six ZIPs passed integrity checks.
- A subsequent exact skills CLI search returned no matching directory result.
  Indexing is still unconfirmed; no delayed follow-up automation was created.

Repository/distribution preparation and GitHub release are complete. External
market review, community posting, directory indexing confirmation and hardware
recording remain open under the prerequisites above.
