#!/usr/bin/env python3
"""Public non-spoiler structural grading checks, no answer values."""
from pathlib import Path
import csv
import re

ROOT=Path(__file__).resolve().parents[1]
main=(ROOT/"questions/INVESTIGATION.md").read_text(encoding="utf-8")
ids=re.findall(r"\bQ([0-9]{2})\s+[—-]", main)
assert ids == [f"{i:02}" for i in range(1,31)],f"Non-canonical, missing or duplicate main questions: {ids}"
with (ROOT/"templates/ANSWER_SHEET.csv").open(newline="",encoding="utf-8") as f:
    sheet=list(csv.DictReader(f))
assert [x["question_id"] for x in sheet]==[f"Q{i:02}" for i in range(1,31)]
assert all(not x["answer"] for x in sheet), "Student answer sheet leaked an answer"
extra=(ROOT/"questions/STATIC_GRADING_CANDIDATE.md").read_text(encoding="utf-8")
assert "retired" in extra and "one active" in (ROOT/"docs/GRADER_HANDOFF.md").read_text(encoding="utf-8").lower()
print("PASS: 30 unique canonical exact-answer prompts, blank grading sheet and no active alternative")
