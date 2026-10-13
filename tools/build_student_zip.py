#!/usr/bin/env python3
"""Reproducibly assemble or validate the spoiler-free Sherlock student archive.

This is an AUTHOR utility. Requires only Python 3 standard library.
Never package instructor solutions, hidden GitHub files, or untracked secret files.
"""
from __future__ import annotations
from pathlib import Path
import argparse
import hashlib
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "downloads" / "The-Silent-Network-Architect-Student.zip"
PUBLIC_ROOTS = ("docs", "evidence", "questions", "templates", "manifest")
PUBLIC_SINGLES = ("README.md", "START_HERE.md", "BEACON-OWNERSHIP.md",
                  "tools/validate_evidence.py", "tools/workbench.py",
                  "tools/generate_synthetic_pcap.py", "tools/packet_inspector.py")

def expected() -> dict[str, bytes]:
    files = {path: ROOT.joinpath(path).read_bytes() for path in PUBLIC_SINGLES}
    for folder in PUBLIC_ROOTS:
        for path in sorted((ROOT / folder).rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                rel = path.relative_to(ROOT).as_posix()
                if rel.lower().endswith((".pyc", ".tmp", ".bak")):
                    continue
                files[rel] = path.read_bytes()
    for path in files:
        low = path.lower()
        if any(x in low for x in ("answer_key", "instructor_solution", "private", "walkthrough_solutions")):
            raise ValueError(f"Potentially confidential source in student archive: {path}")
    return dict(sorted(files.items()))

# README.md has a publisher-only visual header on GitHub. The already
# released student ZIP predates that header. Accept this *exact* HTML prefix
# only; all underlying case instructions and all other ZIP members must remain
# byte-for-byte identical to the repository.
BEACON_GITHUB_HEADER = "<div align=\"center\">\n  <img src=\"https://raw.githubusercontent.com/Centinell2025/the-last-evidence-standing/main/branding/BEACON_SEAL.png\" alt=\"Beacon of the Eagle LLC — logotipo corporativo\" width=\"165\" />\n  <p><strong>BEACON OF THE EAGLE LLC</strong><br/><strong>CENTINELL SUITE DEFENSE</strong></p>\n</div>\n\n".encode("utf-8")

def same_student_content(name: str, packaged: bytes, repository: bytes) -> bool:
    if packaged == repository:
        return True
    return (name == "README.md"
            and repository.startswith(BEACON_GITHUB_HEADER)
            and packaged == repository[len(BEACON_GITHUB_HEADER):])

def check(files: dict[str, bytes]) -> None:
    with zipfile.ZipFile(OUTPUT, "r") as z:
        actual = z.namelist()
        if len(actual) != len(set(actual)):
            raise ValueError("Duplicate ZIP member")
        if set(actual) != set(files):
            missing = sorted(set(files)-set(actual))
            stale = sorted(set(actual)-set(files))
            raise ValueError(f"Missing from ZIP: {missing}; extra in ZIP: {stale}")
        if z.testzip() is not None:
            raise ValueError("CRC failure in student ZIP")
        for name, content in files.items():
            if not same_student_content(name, z.read(name), content):
                raise ValueError(f"Byte mismatch for {name}")
    print(f"PASS: {len(files)} student ZIP members and CRC; exact parity except strict GitHub-only Beacon logo prefix")

def build(files: dict[str, bytes]) -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(prefix="student_", suffix=".zip",
                                     dir=OUTPUT.parent, delete=False) as temp:
        temp_path = Path(temp.name)
    try:
        with zipfile.ZipFile(temp_path, "w", compression=zipfile.ZIP_DEFLATED,
                             compresslevel=7) as z:
            for name, content in files.items():
                info = zipfile.ZipInfo(name, date_time=(2026, 10, 12, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                z.writestr(info, content, compress_type=zipfile.ZIP_DEFLATED)
        temp_path.replace(OUTPUT)
        check(files)
    finally:
        temp_path.unlink(missing_ok=True)

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="Verify current committed student ZIP")
    group.add_argument("--write", action="store_true", help="Rebuild from tracked participant sources")
    a = p.parse_args()
    sources = expected()
    if a.check:
        check(sources)
    else:
        build(sources)
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
