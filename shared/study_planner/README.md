# Study Planner

## 1. Overview

The Study Planner is a Python command-line application that helps students organise their study tasks and allocate available study time.

It reads task information from a CSV file, prioritises tasks based on the selected date, allocates available study hours, and displays the resulting study plan.

## 2. Features

- **CSV Input:** Read study tasks from a CSV file.
- **Task Prioritisation:** Arrange tasks according to their priority and deadlines.
- **Time Allocation:** Allocate available study hours to prioritised tasks.
- **Readable Output:** Display the allocated study blocks in the terminal.
- **Configurable Study Budget:** Specify the number of available study hours.
- **Reproducible Planning:** Specify a reference date for consistent prioritisation.
- **Input Validation:** Validate command-line arguments and report file or data errors.

## 3. Requirements

- Python 3.10 or later.
- Run commands from the repository root.
- Install the testing and code-quality tools if needed:

```bash
python -m pip install pytest ruff
```

## 4. Project Structure

```text
shared/
├── contract.py
└── study_planner/
    ├── __init__.py
    ├── __main__.py
    ├── parse.py
    ├── prioritise.py
    ├── allocate.py
    ├── render.py
    ├── sample_tasks.csv
    └── README.md
```

- `contract.py`: Defines shared data structures used by the planner.
- `__main__.py`: Provides the command-line interface and coordinates the planning workflow.
- `parse.py`: Reads and validates task data from CSV.
- `prioritise.py`: Orders tasks for planning.
- `allocate.py`: Allocates the available study time.
- `render.py`: Formats allocated study blocks for terminal output.
- `sample_tasks.csv`: Provides sample input data.
- `README.md`: Documents setup, usage, and input requirements.

## 5. Input Format

The input CSV must contain the following columns in this order:

| Column | Description | Example |
|---|---|---|
| `title` | Name of the study task | `Review Python` |
| `importance` | Importance value of the task | `5` |
| `effort_h` | Estimated effort in hours | `2.0` |
| `deadline` | Task deadline in `YYYY-MM-DD` format | `2026-10-30` |

Example CSV:

```csv
title,importance,effort_h,deadline
Review Python,5,2.0,2026-10-22
Complete assignment,4,3.5,2026-10-24
Prepare for exam,5,5.0,2026-10-28
Practice algorithms,3,1.5,2026-10-30
```

A CSV file should follow the required schema and contain valid task data.

## 6. Usage

Run all commands from the repository root.

### 6.1. Display Help

```bash
python -m shared.study_planner --help
```

This command displays the available command-line arguments.

### 6.2. Run with the Default Sample

```bash
python -m shared.study_planner --hours 2 --today 2026-10-26
```

The application uses the bundled sample CSV when no input path is provided.

### 6.3. Run with a Custom CSV File

```bash
python -m shared.study_planner path/to/tasks.csv --hours 3 --today 2026-10-26
```

Replace `path/to/tasks.csv` with the path to your CSV file.

### 6.4. Command-Line Arguments

| Argument | Description | Default |
|---|---|---|
| `csv_path` | Path to the input CSV file | Bundled sample CSV |
| `--hours` | Available study time in hours | `2.0` |
| `--today` | Reference date in `YYYY-MM-DD` format | Current date |

The `--hours` argument must be a finite, non-negative number. The `--today` argument must be a valid ISO date.

## 7. Output

The application displays the allocated study blocks in the terminal. Each line contains a task title and its allocated study time.

Example output format:

```text
Review Python: 2 hours
```

The actual output depends on the input CSV, reference date, available hours, and task allocation logic.

Tasks that cannot be allocated study time may not appear in the rendered output.

## 8. Error Handling

The command-line interface handles common input errors, including:

- Missing or inaccessible input files.
- Invalid CSV data.
- Invalid command-line arguments.
- Invalid or negative study-hour values.
- Invalid reference dates.

Argument errors are handled by `argparse`. File and data errors are reported to standard error with a non-zero exit status.

## 9. Testing

Run the complete test suite from the repository root:

```bash
python -m pytest -q .
```

Check code quality with Ruff:

```bash
ruff check .
```

To verify the CLI manually:

```bash
python -m shared.study_planner --help
python -m shared.study_planner --hours 2 --today 2026-10-26
```

Record the actual test results and any existing failures when reporting verification status.

## 10. Demo

For a step-by-step demonstration, refer to the team demo guide at `docs/demo.md`, if available.

The demo should show the input CSV, CLI options, a successful run, the generated output, and the test results.

## 11. Notes

- Run commands from the repository root unless otherwise specified.
- Use `--today` to make demonstrations reproducible.
- Ensure that CSV headers and values follow the required schema.
- Verify behavior against the current implementation before documenting additional features.
