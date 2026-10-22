import csv
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_CSV = PROJECT_ROOT / "shared" / "study_planner" / "sample_tasks.csv"

EXPECTED_COLUMNS = ["title", "importance", "effort_h", "deadline"]


def test_sample_csv_exists():
    assert SAMPLE_CSV.is_file()


def test_sample_csv_has_expected_columns_and_rows():
    with SAMPLE_CSV.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

        assert reader.fieldnames == EXPECTED_COLUMNS
        assert len(rows) >= 1


def test_sample_csv_rows_have_valid_values():
    with SAMPLE_CSV.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        assert row["title"].strip()
        assert 1 <= int(row["importance"]) <= 5
        assert float(row["effort_h"]) > 0
        parsed_date = date.fromisoformat(row["deadline"])
        assert parsed_date.isoformat() == row["deadline"]
