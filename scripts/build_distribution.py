#!/usr/bin/env python3
"""Build deterministic plugin/skill ZIPs and verify every archived file."""

import argparse
import hashlib
import json
import stat
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("m5stack-assistant", "m5stack-firmware-query", "uiflow2-coder", "uiflow2-ui-designer")


def files_under(folder):
    paths = []
    for path in sorted(folder.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Unexpected symlink: {path.relative_to(ROOT)}")
        if path.is_file():
            if any(part.startswith(".") or part == "__pycache__" for part in path.relative_to(folder).parts):
                raise ValueError(f"Unexpected hidden/runtime file: {path.relative_to(ROOT)}")
            paths.append(path)
    return paths


def write_archive(output, root_name, paths, relative_to):
    if output.exists():
        raise ValueError(f"Refusing to overwrite existing artifact: {output.name}")
    expected = {}
    expected_modes = {}
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(paths):
            relative = path.relative_to(relative_to).as_posix()
            name = root_name + "/" + relative
            data = path.read_bytes()
            expected[name] = hashlib.sha256(data).hexdigest()
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 8, 0, 0, 0))
            info.create_system = 3
            mode = 0o755 if path.stat().st_mode & 0o111 else 0o644
            expected_modes[name] = mode
            info.external_attr = (stat.S_IFREG | mode) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data, compresslevel=9)
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None or len(archive.namelist()) != len(expected):
            raise ValueError(f"Archive integrity failure: {output.name}")
        actual = {name: hashlib.sha256(archive.read(name)).hexdigest() for name in archive.namelist()}
        if actual != expected:
            raise ValueError(f"Archive content differs from sources: {output.name}")
        for info in archive.infolist():
            if (info.external_attr >> 16) & 0o777 != expected_modes[info.filename]:
                raise ValueError(f"Archive permissions differ from sources: {output.name}")
    return {"file": output.name, "fileCount": len(expected), "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}


def build(output_dir):
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    mcp = json.loads((ROOT / "mcp.json").read_text(encoding="utf-8"))
    if manifest["name"] != "m5stack-skills" or manifest["author"]["name"] != "yuyun2000":
        raise ValueError("Plugin identity differs from the intended publisher")
    if mcp["mcpServers"]["m5stack-docs"] != {"type": "sse", "url": "https://mcp.m5stack.com/sse"}:
        raise ValueError("Unexpected MCP configuration")
    for field in ("composerIcon", "logo"):
        path = manifest["extensions"]["com.openai"]["interface"][field]
        if not path.startswith("./") or ".." in Path(path).parts or not (ROOT / path).is_file():
            raise ValueError(f"Invalid plugin asset: {field}")
    if {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()} != set(NAMES):
        raise ValueError("Unexpected skill set")
    output_dir.mkdir(parents=True, exist_ok=True)
    version = manifest["version"]
    if not version or any(c not in "0123456789.-abcdefghijklmnopqrstuvwxyz" for c in version):
        raise ValueError("Invalid artifact version")
    artifact_names = [f"m5stack-skills-{version}.zip", f"m5stack-launch-kit-{version}.zip", "SHA256SUMS.txt"]
    artifact_names += [f"{name}-{version}.zip" for name in NAMES]
    if any((output_dir / name).exists() for name in artifact_names):
        raise ValueError("Output directory already contains distribution artifacts")
    paths = [ROOT / name for name in (
        "plugin.json", "mcp.json", "LICENSE", "THIRD_PARTY_NOTICES.md", "CONTRIBUTING.md", "requirements-dev.txt",
        "PRIVACY.md", "TERMS.md", "README.md", "README.zh-CN.md", "skills-lock.json",
    )]
    paths += files_under(ROOT / "assets") + files_under(ROOT / "licenses")
    paths += files_under(ROOT / "scripts")
    paths += [ROOT / "docs" / name for name in ("distribution.md", "launch-kit.md", "submission.md")]
    for name in NAMES:
        paths += files_under(ROOT / "skills" / name)
    results = [write_archive(output_dir / f"m5stack-skills-{version}.zip", "m5stack-skills", paths, ROOT)]
    for name in NAMES:
        results.append(write_archive(output_dir / f"{name}-{version}.zip", name, files_under(ROOT / "skills" / name), ROOT / "skills" / name))
    launch_paths = [ROOT / "docs/launch-kit.md", ROOT / "LICENSE"] + files_under(ROOT / "assets/promo")
    results.append(write_archive(output_dir / f"m5stack-launch-kit-{version}.zip", "m5stack-launch-kit", launch_paths, ROOT))
    checksums = "".join(f"{result['sha256']}  {result['file']}\n" for result in results)
    checksum_file = output_dir / "SHA256SUMS.txt"
    checksum_file.write_text(checksums, encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    build(parser.parse_args().output_dir.resolve())
