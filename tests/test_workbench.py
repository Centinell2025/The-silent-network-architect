#!/usr/bin/env python3
"""Smoke tests proving the downloaded Sherlock is navigable without special libraries."""
from pathlib import Path
import subprocess
import sys
import csv

ROOT = Path(__file__).resolve().parents[1]
WORKBENCH = ROOT / "tools" / "workbench.py"
SHEET = ROOT / "templates" / "ANSWER_SHEET.csv"

def run(*args: str) -> str:
    p = subprocess.run([sys.executable, str(WORKBENCH), *args],
                       cwd=ROOT, capture_output=True, text=True, timeout=20)
    assert p.returncode == 0, p.stderr
    return p.stdout

assert "Repository evidence inventory" in run("inventory")
assert "Matches displayed" in run("search", "nonexistent_test_keyword", "--limit", "2")
assert "Fields:" in run("inspect", "evidence/06_control_plane/controller_audit.csv")
assert "Displayed" in run("timeline", "--after", "2026-10-06T02:00:00Z",
                          "--before", "2026-10-06T02:20:00Z", "--limit", "5")
digest = run("hash", "evidence/09_export/network-audit-bundle.zip").split()[0]
assert len(digest) == 64 and all(c in "0123456789abcdef" for c in digest)
with SHEET.open(newline="", encoding="utf-8") as f:
    sheet = list(csv.DictReader(f))
assert [r["question_id"] for r in sheet] == [f"Q{i:02}" for i in range(1, 31)]
assert not any(r["answer"] for r in sheet), "Student answer sheet must be blank"
print("PASS: workbench inventory/search/inspect/timeline/hash; blank 30-answer worksheet")
