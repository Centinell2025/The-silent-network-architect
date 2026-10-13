#!/usr/bin/env python3
"""Maintain the content-addressed SHA-256 evidence manifest (author-side only)."""
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"manifest/SHA256SUMS.txt"
def main():
    lines=MANIFEST.read_text(encoding="utf-8").splitlines()
    original={}
    for line in lines:
        if not line or line.startswith("#"):continue
        digest,path=line.split("  ",1)
        original[path]=digest
    for path,digest in original.items():
        f=ROOT/path
        if not f.is_file():raise ValueError("Manifest file missing: "+path)
        current=hashlib.sha256(f.read_bytes()).hexdigest()
        if current!=digest:raise ValueError("Existing file unexpectedly changed: "+path)
    for path in sorted((ROOT/"evidence").rglob("*")):
        if path.is_file():
            original[path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
    content="# SHA-256 checksums for fictional Sherlock evidence (excludes manifest itself)\n"
    content+="".join(f"{digest}  {path}\n" for path,digest in sorted(original.items()))
    MANIFEST.write_text(content,encoding="utf-8")
    print("PASS: preserved existing digests; indexed",len(original),"evidence artifacts")
if __name__=="__main__":main()
