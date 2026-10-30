# Sync the current UIFlow2 coding skill

Goal: import the audited current Skill Hub `uiflow2-coder` package and publish
the repository and updated distributions without altering the other skills.

- [x] Refresh and validate the source archive; preserve the repository LICENSE
  and script executable modes while importing only changed and added files.
- [x] Update source/published hashes and package version to 0.1.1; document the
  current source snapshot separately from the original October 8 import.
- [x] Run skill/repository checks, Python parsing, document search and archive
  integrity/reproducibility checks; audit the staged public diff.
- [ ] Commit/push main, verify remote commit and GitHub CI, publish v0.1.1
  artifacts and compare downloaded asset hashes.

Audit baseline: the October 30 12:12 CST Hub package has 385 files, adding nine
documents and modifying 101 files against the previous 376-file source snapshot.
There are no deletions. The other three source content hashes are unchanged.

Keep upstream MIT notices and public packaging adjustments. Display rotation
guidance is firmware-dependent; preserve the new documentation's migration
notes. No hardware execution or device state changes are part of this sync.

Validation completed: official skill frontmatter check; repository hashes,
links, encoding and script parsing; seven existing firmware-query tests;
search for new controller/driver documents; Codex copy installation (410 files)
and Claude Code symlink installation of the UI pair (397 files); unchanged
source hashes for the other three skills; reproducible ZIP builds with full
source/member content and permission comparisons. No hardware run was performed.
