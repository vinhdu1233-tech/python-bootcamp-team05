# Week 3 — Individual exercises (Member 1)

- **W3-1 `dates.py`**: `parse_due(text, today)` recognises ISO dates, tomorrow, days ahead, and future weekdays; unknown expressions raise `ValueError`.
- **W3-2 `log_stats.py`**: `analyse(pairs)` returns route request counts, nearest-rank p95 latency per route, and the route with the highest p95 (alphabetical tie-break).
- **W3-3 `cli.py`**: the planner reads task CSV through Week 2 `load_tasks`, and reuses the team's Week 2 `prioritise` and `allocate` functions.

## Run the CLI

From the repository root:

```bash
python -m members.vinhdu1233_tech.w3.cli members/vinhdu1233_tech/w2/sample_tasks.csv --hours 2 --today 2026-10-26
```

The tutorial's example `samples/tasks.csv` will be supported once the separate sample-CSV team PR (#30) is merged.

## Run individual tests

```bash
python -m pytest -q members/vinhdu1233_tech/w3/test_w3.py
ruff check members/vinhdu1233_tech/w3
```

## W3-4: Three Python differences from C++

1. Python's `datetime.date` and `timedelta` handle calendar arithmetic directly, without manual day/month overflow handling.
2. Python's `Counter` and `defaultdict` let me tally routes and group latency samples without explicit map insert/check boilerplate.
3. Python's `argparse` provides a reusable CLI parser, help text, and validation, rather than manually processing `argc` and `argv` as in C++.

The functions in my Week 1–3 individual folders are annotated and documented; W3-4 also refines typing in `w1/grades.py` and `w2/errors.py`.

## AI assistance disclosure

ChatGPT generated initial Week 3 implementations, test cases, and documentation, and pushed them through the connected GitHub account. This is acknowledged in the PR and `docs/ai-use-log.md`. The member must read, verify, and be able to explain the code before the individual defence; a passing test suite does not replace that review.
