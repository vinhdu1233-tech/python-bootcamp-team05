# CSC10014 Python Bootcamp — Team 05

## Overview

This repository contains the Python homework for Weeks 1, 2, and 3 of CSC10014.

## Team Guidelines

- Each member completes the individual weekly exercises in their own folder.
- Individual folders are named after GitHub usernames, replacing hyphens with underscores.
- Each member creates a separate branch and pull request.
- Commit after each exercise with a clear commit message.
- Run the available tests before submitting a pull request.
- Each pull request must be reviewed by another team member before merging.

## Directory Structure

- `members/` — Individual homework organized by member and week.
- `shared/contract.py` — Shared `Task` and `Block` dataclasses.
- `shared/study_planner/` — Shared study-planner package; modules are being integrated.
- `shared/study_planner/sample_tasks.csv` — Sample study tasks for testing and demonstration.
- `tests/` — Automated tests.
- `PROGRESS.md` — Weekly progress, pull requests, and review tracking.

## Week 2: Study Planner

The Week 2 project is organized into modules with separate responsibilities:

| Module | Responsibility | Status |
|---|---|---|
| `parse.py` | Read and validate task data from CSV | Pending integration |
| `prioritise.py` | Prioritise tasks for study planning | Pending integration |
| `allocate.py` | Allocate available study time to tasks | Pending integration |
| `render.py` | Format or display the resulting plan | Pending integration |
| `contract.py` | Define the shared `Task` and `Block` data structures | Available |

The study-planner modules should use `Task` and `Block` from `shared/contract.py` rather than defining duplicate data structures.

### Sample CSV Schema

The sample file is `shared/study_planner/sample_tasks.csv`.

It uses these columns in this exact order:

| Column | Meaning | Example |
|---|---|---|
| `title` | Task name | Review Python |
| `importance` | Task importance | `5` |
| `effort_h` | Estimated effort in hours | `2.0` |
| `deadline` | Deadline in ISO date format (`YYYY-MM-DD`) | `2026-10-22` |

Example:

```csv
title,importance,effort_h,deadline
Review Python,5,2.0,2026-10-22
Complete assignment,4,3.5,2026-10-24
Prepare for exam,5,5.0,2026-10-28
Practice algorithms,3,1.5,2026-10-30
```

### Setup

Install the testing and code-quality tools:

```bash
python -m pip install pytest ruff
```

Run commands from the repository root.

### Run Tests

Run the complete available test suite:

```bash
python -m pytest -q .
```

### Check Code Quality

Run Ruff:

```bash
ruff check .
```

### Current Usage

The sample CSV can be inspected with Python's standard CSV reader:

```python
import csv
from pathlib import Path

csv_path = Path("shared/study_planner/sample_tasks.csv")

with csv_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)
    for row in reader:
        print(row)
```

This example demonstrates reading the sample data only. It does not imply that the study-planner parser, allocation workflow, or command-line interface is already implemented.

Once the shared modules are integrated, add working examples and package-import instructions based on the final APIs.

## Homework Tracking

Each member should create a GitHub issue, submit their work through a pull request, and request a review from another team member.

## Academic Integrity

Each member is responsible for understanding and explaining their own code. Any AI-generated code or substantial AI assistance retained in the submission must be disclosed according to the course requirements.
