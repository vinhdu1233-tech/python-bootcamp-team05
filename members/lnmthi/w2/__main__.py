
from pathlib import Path

from .io_utils import load_tasks


def main():
    folder = Path(__file__).parent
    csv_path = folder / "task.csv"

    tasks = load_tasks(csv_path)

    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
