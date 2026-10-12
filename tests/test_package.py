#!/usr/bin/env python3
"""Offline regression tests for the public Sherlock student ZIP; no answer key included."""
from pathlib import Path
import hashlib
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "downloads" / "The-Silent-Network-Architect-Student.zip"
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
        assert hashlib.sha256(z.read(name)).digest() == hashlib.sha256(path.read_bytes()).digest(), (
            f"Packaged file differs from repository copy: {name}"
        )
    with zipfile.ZipFile(z.open("evidence/09_export/network-audit-bundle.zip")) as inner:
        assert inner.testzip() is None
        assert len(inner.namelist()) == 2
print(f"PASS: student ZIP CRC, 30 questions, {len(names)} package/source byte matches and solution isolation")
