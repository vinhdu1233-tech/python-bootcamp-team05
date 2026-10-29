# Study Planner Demo

## 1. Overview

The Study Planner is a command-line application that helps users organise study tasks based on their importance, estimated effort, deadlines, and available study time.

The application reads tasks from a CSV file, prioritises them, allocates study time, and displays the resulting study plan.

## 2. Requirements

- Python 3.10 or later
- A terminal or command prompt
- The project dependencies installed, if required by the repository

Run all commands from the repository root directory.

## 3. Demo 1: Display Help

Run the following command to see the available command-line options:

```bash
python -m shared.study_planner --help
```

The help message describes the CSV input path and the available options, including `--hours` and `--today`.

## 4. Demo 2: Run with Sample Data

Run the application using the default sample CSV file:

```bash
python -m shared.study_planner --hours 2 --today 2026-10-26
```

This command asks the application to create a study plan with a daily time budget of 2 hours, using October 26, 2026, as the planning date.

The application reads the sample tasks, prioritises them, allocates the available study time, and prints the plan.

The exact output depends on the task prioritisation and allocation logic implemented in the project.

## 5. Demo 3: Use a Custom CSV File

Users can provide their own CSV file as the first positional argument.

Example:

```bash
python -m shared.study_planner shared/study_planner/sample_tasks.csv --hours 3 --today 2026-10-26
```

This command uses the specified CSV file and sets the available study time to 3 hours.

### CSV format

The input file must contain the following columns:

| Column | Description |
|---|---|
| `title` | Name of the study task |
| `importance` | Importance value assigned to the task |
| `effort_h` | Estimated effort in hours |
| `deadline` | Task deadline |

Example:

```csv
title,importance,effort_h,deadline
Review Python,5,2,2026-10-28
Complete assignment,4,3,2026-10-30
Prepare for exam,5,4,2026-11-02
Practice algorithms,3,2,2026-11-05
```

## 6. Demo 4: Validate Command-Line Arguments

The application validates the supplied arguments before generating the plan.

For example, a negative time budget should be rejected:

```bash
python -m shared.study_planner --hours -1 --today 2026-10-26
```

An invalid date should also be rejected:

```bash
python -m shared.study_planner --hours 2 --today invalid-date
```

When an error occurs, the application displays an error message instead of generating a normal study plan. Invalid command-line arguments may be reported by `argparse`.

## 7. Demo 5: Run Tests and Code Checks

Run the test suite from the repository root:

```bash
python -m pytest -q .
```

If Ruff is installed in the project environment, check code quality with:

```bash
python -m ruff check .
```

To verify formatting, run:

```bash
python -m ruff format --check .
```

Confirm that the commands complete successfully before recording the demo results.

## 8. Suggested Screenshots

For a demonstration or pull request, capture the following screenshots:

1. The output of `python -m shared.study_planner --help`.
2. A successful run using the sample CSV file.
3. A successful run using a custom time budget.
4. An invalid-argument example showing the error message.
5. The test and lint commands completing successfully.

Only include screenshots of commands that have actually been executed.

## 9. Summary

This demo demonstrates how to launch the Study Planner, configure the available study time and planning date, provide a CSV file, handle invalid input, and run the project's tests and code-quality checks.
