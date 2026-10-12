# Blind trial protocol — independent investigators

**Purpose:** establish whether the Sherlock is uniquely solvable, fair, enjoyable and genuinely Insane-level, without giving participants author answers.

Recruit two experienced DFIR analysts with no prior access to the instructor package or old public solution hints. Supply only the current student ZIP (and public solver quick-start), **not** the author's replay script, screenshots, private expected-answer CSV or full public repository history. Record the exact ZIP SHA-256, investigator environment and tool versions.

Have each analyst privately record time to find the unauthorized controller operation, to identify the monitoring blackout, to correlate transfer evidence, and to reach the last question. Score Q01–Q30 on the exact answer plus original source support; write down conflicting interpretations, hints requested and cases where only one log is enough. Ask for a short supported / inconclusive / unsupported incident disposition.

After both sessions, compare answers to the private instructor key. Mark any question with ambiguous answers, unjustified assumptions or inaccessible source data as **failed**, then revise the challenge and re-test. Only externally obtained independent results can close this gate; the author running their own answer-check script does not count.

Recommended metrics: exact-answer accuracy, elapsed solve time, number of hints, independently reproduced hash and UTC calculations, count of ambiguous prompts, realism score (1–5) and evaluator recommendation. These are author evaluation metrics, **not** official HTB measurements.

**Do not report this trial as completed until actual independent reviewer results exist.**
