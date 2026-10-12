# CSC10014 Python Bootcamp — Team 05

## Overview

This folder contains the Python homework for Weeks 1, 2, and 3 of CSC10014.

## Team Guidelines

- Each member completes the individual weekly exercises in their own folder.
- Individual folders are named after GitHub usernames, replacing hyphens with underscores.
- Each member creates a separate branch and pull request.
- Commit after each exercise with a clear commit message.
- Run the available tests before submitting a pull request.
- Each pull request must be reviewed by another team member before merging.

## Directory Structure

- `members/` — Individual homework organized by member and week.
- `shared/` — Shared team code for Weeks 2 and 3.
- `tests/` — Instructor-provided automated tests.
- `PROGRESS.md` — Weekly progress, pull requests, and review tracking.

## Running Tests

Install the required testing tools:

```bash
python -m pip install pytest ruff
```

Run the bootcamp tests after the instructor-provided tests have been added:

```bash
python -m pytest -q python-bootcamp
```

Check code quality:

```bash
ruff check python-bootcamp
```

## Homework Tracking

Each member should create a GitHub issue, submit their work through a pull request, and request a review from another team member.

## Academic Integrity

Each member is responsible for understanding and explaining their own code. Any AI-generated code retained in the submission must be disclosed according to the course requirements.