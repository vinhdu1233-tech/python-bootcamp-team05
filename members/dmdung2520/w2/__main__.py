from pathlib import Path

from members.dmdung2520.w2.io_utils import load_tasks


def main():
    csv_path = Path(__file__).parent / "tasks.csv"

    if not csv_path.exists():
        print(f"Cannot find task file: {csv_path}")
        return

    tasks = load_tasks(csv_path)

    for task in tasks:
        print(
            f"Title: {task.title}, "
            f"Importance: {task.importance}, "
            f"Effort: {task.effort_h} hours, "
            f"Deadline: {task.deadline}"
        )


if __name__ == "__main__":
    main()