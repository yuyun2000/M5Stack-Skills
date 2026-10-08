# Contributing

Keep changes focused on the skill's behavior, authoritative references, or
reproducible problems. Include the affected product and firmware version when
reporting UIFlow2 issues. Remove credentials and personal/customer data from
reports and examples.

## Validate locally

Python 3.10+, Node.js 18+, and Bash are needed for the repository checks.
PyYAML is a development dependency only; the firmware query CLI uses the Python
standard library.

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
PYTHONDONTWRITEBYTECODE=1 python3 skills/m5stack-firmware-query/scripts/test_m5stack_firmware_query.py
git diff --check
```

The validator checks frontmatter, complete package manifests, local Markdown
links, UTF-8 encoding, unexpected artifacts, script syntax, and high-confidence
credential patterns. It does not replace a manual public-release audit or prove
that generated code runs on hardware. The GitHub workflow runs offline checks;
live API availability is checked separately.

## Updating a skill

1. Obtain the complete source package and record its timestamp, file count,
   archive SHA-256, and deterministic content SHA-256. Do not publish private
   catalog metadata, comments, service addresses, or credentials.
2. Before extracting, check ZIP integrity, a single skill-named top-level
   directory, duplicate entries, path traversal, and symlinks.
3. Compare the full source tree against the published package. Preserve API
   documentation, examples, upstream notices, sibling-skill links, and script
   executable bits. Review deletions as well as additions.
4. Record source information and any intentional public-package adjustments in
   `skills-lock.json`. Run `python3 scripts/validate_skills.py --update-manifest`
   to refresh the published file counts and content hashes after an intentional
   change. The command does not change source provenance.
5. Run local validation and the relevant existing tests. For runtime changes,
   perform a bounded smoke test and record actual evidence. Do not flash devices,
   mutate services, or submit external feedback as part of an offline test.
6. Review the complete staged diff for sensitive data, topology, runtime files,
   encoding damage, whitespace, and unrelated changes before publishing.

The manifest hashes each sorted file as `relative/path + NUL + SHA256(file) + LF`,
then hashes the concatenated UTF-8 records. Permissions are checked separately
and are not part of this content digest. Preserve upstream attribution and
license notices when copying or adapting material.
