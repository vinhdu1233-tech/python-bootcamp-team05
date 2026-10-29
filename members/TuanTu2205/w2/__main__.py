from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load sample study tasks from CSV and display their information."""
    csv_path = Path(__file__).with_name("sample_tasks.csv")
    tasks = load_tasks(csv_path)

    for task in tasks:
        print(
            f"{task.title}: importance={task.importance}, "
            f"effort={task.effort_h}h, deadline={task.deadline}"
        )


if __name__ == "__main__":
    main()
