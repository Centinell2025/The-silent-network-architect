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
                  "tools/validate_evidence.py", "tools/workbench.py")

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
            if hashlib.sha256(z.read(name)).digest() != hashlib.sha256(content).digest():
                raise ValueError(f"Byte mismatch for {name}")
    print(f"PASS: {len(files)} student ZIP members, CRC and exact repository parity")

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
