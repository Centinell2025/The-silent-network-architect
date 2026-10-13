#!/usr/bin/env python3
"""Offline regression tests for the public Sherlock student ZIP; no answer key included."""
from pathlib import Path
import hashlib
import re
import zipfile
import sys

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "downloads" / "The-Silent-Network-Architect-Student.zip"
sys.path.insert(0, str(ROOT))
from tools.build_student_zip import same_student_content, BEACON_GITHUB_HEADER
REQUIRED = {
    "README.md",
    "docs/NETWORK_ARCHITECTURE.md",
    "docs/HOSTS_SERVICES_AND_IDENTITIES.md",
    "docs/CVE_PII_AND_EVIDENCE_PROVENANCE.md",
    "docs/HTB_AUTHOR_READINESS.md",
    "questions/INVESTIGATION.md",
    "manifest/SHA256SUMS.txt",
    "evidence/09_export/network-audit-bundle.zip",
}
with zipfile.ZipFile(PACK) as z:
    names = z.namelist()
    assert len(names) == len(set(names)), "Duplicate ZIP members"
    assert z.testzip() is None, "Invalid ZIP CRC"
    assert REQUIRED <= set(names), "Missing student package resources"
    assert not any(re.search(r"(answer.?key|instructor.?solution|walkthrough)", n, re.I)
                   for n in names), "Instructor solution accidentally public"
    questions = z.read("questions/INVESTIGATION.md").decode("utf-8")
    assert len(re.findall(r"\bQ[0-9]{2}\s+[—-]", questions)) == 30
    for name in names:
        path = ROOT / name
        assert path.is_file(), f"Packaged source is not tracked: {name}"
        assert same_student_content(name, z.read(name), path.read_bytes()), (
            f"Packaged file differs from repository copy: {name}"
        )
    # A changed investigation instruction or extra HTML cannot bypass parity.
    original = z.read("README.md")
    published = (ROOT / "README.md").read_bytes()
    assert published.startswith(BEACON_GITHUB_HEADER), "GitHub publisher logo missing"
    assert same_student_content("README.md", original, published)
    assert not same_student_content("README.md", original, published + b"UNVERIFIED-EXTRA-TEXT")
    assert not same_student_content("questions/INVESTIGATION.md", original, published)
    with zipfile.ZipFile(z.open("evidence/09_export/network-audit-bundle.zip")) as inner:
        assert inner.testzip() is None
        assert len(inner.namelist()) == 2
print(f"PASS: student ZIP CRC, 30 questions, {len(names)} strict case-source matches, controlled Beacon header and solution isolation")
