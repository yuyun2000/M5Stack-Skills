#!/usr/bin/env python3
"""Offline checks for published M5Stack skill packages."""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "uiflow2-coder", "uiflow2-ui-designer",
    "m5stack-assistant", "m5stack-firmware-query",
}
SECRET = re.compile(
    r"sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|"
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
)


def content_digest(folder):
    files = sorted(p for p in folder.rglob("*") if p.is_file())
    records = "".join(
        f"{p.relative_to(folder).as_posix()}\0"
        f"{hashlib.sha256(p.read_bytes()).hexdigest()}\n" for p in files
    )
    return len(files), hashlib.sha256(records.encode("utf-8")).hexdigest()


def validate(update_manifest=False):
    errors = []
    folders = {p.name: p for p in (ROOT / "skills").iterdir() if p.is_dir()}
    if set(folders) != EXPECTED:
        errors.append("Unexpected or missing skill folders")
    manifest_path = ROOT / "skills-lock.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = {entry["name"]: entry for entry in manifest["skills"]}
    if set(entries) != EXPECTED or len(entries) != len(manifest["skills"]):
        errors.append("Unexpected, duplicate or missing manifest entries")

    for name, folder in sorted(folders.items()):
        entrypoint = folder / "SKILL.md"
        if not entrypoint.is_file():
            errors.append(f"{name}: missing SKILL.md")
            continue
        text = entrypoint.read_text(encoding="utf-8")
        header = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        metadata = yaml.safe_load(header[1]) if header else None
        if not isinstance(metadata, dict) or metadata.get("name") != name:
            errors.append(f"{name}: invalid YAML frontmatter or name")
        elif not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
            errors.append(f"{name}: missing description")
        elif len(metadata["description"]) > 1024:
            errors.append(f"{name}: description exceeds 1024 characters")
        if not (folder / "LICENSE").is_file():
            errors.append(f"{name}: missing portable license notice")
        count, digest = content_digest(folder)
        if name not in entries:
            continue
        entry = entries[name]
        if update_manifest:
            entry["publishedFileCount"] = count
            entry["publishedContentSha256"] = digest
        elif (entry["publishedFileCount"], entry["publishedContentSha256"]) != (count, digest):
            errors.append(f"{name}: content differs from published manifest")
        print(f"{name}: {count} files")

    # Check tracked/project content, excluding Git metadata and the optional local venv.
    for path in sorted(ROOT.rglob("*")):
        relative = path.relative_to(ROOT)
        if any(part in {".git", ".venv", "venv", "node_modules"} for part in relative.parts):
            continue
        if path.is_symlink():
            errors.append(f"{relative}: unexpected symlink")
            continue
        if not path.is_file():
            continue
        if path.suffix in {".pyc", ".zip", ".bin", ".elf", ".log"} or path.name.startswith(".env") or path.name == ".DS_Store":
            errors.append(f"{relative}: unexpected runtime/archive file")
        data = path.read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"{relative}: not UTF-8 text")
            continue
        if data.startswith(b"\xef\xbb\xbf") or "\ufffd" in text:
            errors.append(f"{relative}: BOM or replacement character")
        if any(line.rstrip() != line for line in text.splitlines()):
            errors.append(f"{relative}: trailing whitespace")
        if SECRET.search(text):
            errors.append(f"{relative}: possible credential; inspect without printing it")
        if path.suffix == ".md":
            # Links in these packages use standard inline Markdown destinations.
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                if not (path.parent / unquote(url.path)).exists():
                    errors.append(f"{relative}: missing local link {target}")
        if path.suffix == ".py":
            try:
                compile(text, str(relative), "exec")
            except SyntaxError as exc:
                errors.append(f"{relative}: {exc}")
        elif path.suffix in {".js", ".mjs", ".sh"}:
            command = ["bash", "-n", str(path)] if path.suffix == ".sh" else ["node", "--check", str(path)]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode:
                errors.append(f"{relative}: syntax check failed: {result.stderr.strip()}")
        if data.startswith(b"#!") and path.suffix in {".sh", ".py", ".mjs", ".js"} and not path.stat().st_mode & 0o111:
            errors.append(f"{relative}: shebang script is not executable")

    if errors:
        raise SystemExit("\n".join(errors))
    if update_manifest:
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("PASS: metadata, manifests, links, encoding, artifacts, credentials and script syntax")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--update-manifest", action="store_true", help="Refresh published hashes after an intentional change")
    validate(parser.parse_args().update_manifest)
