
from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load and print sample tasks."""
    csv_path = Path(__file__).with_name("sample_tasks.csv")
    tasks = load_tasks(csv_path)

    print("Week 2 Task List")
    print("----------------")

    for task in tasks:
        print(
            f"{task.title} | "
            f"Importance: {task.importance} | "
            f"Effort: {task.effort_h}h | "
            f"Deadline: {task.deadline}"
        )


if __name__ == "__main__":
    main()
