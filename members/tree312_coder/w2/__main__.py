
from pathlib import Path

from .io_utils import load_tasks


def main():
    csv_path = Path(__file__).parent / "sample_tasks.csv"
    tasks = load_tasks(csv_path)

    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
