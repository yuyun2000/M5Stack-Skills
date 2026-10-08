# Public skills repository

Goal: publish the four requested M5Stack skills from Skill Hub as complete,
portable packages in the public M5Stack-Skills repository.

## Plan

- [x] Confirm the empty GitHub repository and fetch its remote state.
- [x] Download the four current Hub archives and validate paths, ZIP integrity,
  symlinks, file counts and uncompressed sizes against live metadata.
- [x] Import complete skill directories under `skills/`; preserve official
  documentation, example code, attribution and cross-skill references.
- [x] Add English/Chinese usage, installation, dependencies, licensing,
  contribution guidance and a source manifest without private Hub details.
- [x] Validate skill metadata, links, encoding, script syntax, offline tests,
  public API smoke tests and the staged public-release diff.
- [ ] Commit and push to `main`; verify the remote commit and CI result.

Done when the public remote contains all four packages and a new user can
identify, install and use each skill from the README. Offline validation and
live smoke-test evidence must be reported separately from hardware validation.

Scope: repository content only. Do not modify the Hub versions or local agent
installations. Do not upload firmware, flash devices or submit test feedback.

## Validation evidence

- Four official skill-creator checks passed; 397 original source files preserved,
  with four portable license files added. Only the two assistant MCP scripts had
  trailing whitespace normalized; their behavior was unchanged.
- Repository validation passed: 401 skill files, deterministic content hashes,
  YAML metadata, local links, UTF-8, artifact/credential patterns, Python parsing,
  Node.js syntax and Bash syntax. The source archives had no unsafe paths,
  duplicate entries or symlinks.
- Both README installation examples were executed in isolated temporary homes;
  all contents/modes matched, and repeat installation refused existing folders.
- All seven existing firmware-query tests passed.
- Public M5Burner `devices` returned API code 200 and 53 records; the assistant
  `knowledge_search` CLI returned official CoreS3 documentation.
- No device execution, visual hardware verification or PowerShell runtime test
  was performed. PowerShell is unavailable on the validation machine.
