
import pytest

from shared.contract import Task
from shared.study_planner.parse import parse_csv


def test_parse_csv(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6,2026-10-30\n"
        "Assignment,4,1.5,2026-10-27\n",
        encoding="utf-8",
    )

    tasks = parse_csv(path)

    assert len(tasks) == 2
    assert isinstance(tasks[0], Task)
    assert tasks[0].title == "DS exam"
    assert tasks[0].importance == 5
    assert tasks[1].effort_h == 1.5


def test_empty_csv(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n",
        encoding="utf-8",
    )

    assert parse_csv(path) == []


def test_invalid_importance(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,9,6,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 2"):
        parse_csv(path)


def test_invalid_deadline(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6,invalid-date\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 2"):
        parse_csv(path)

@pytest.mark.parametrize("effort", ["nan", "inf", "-inf"])
def test_non_finite_effort(tmp_path, effort):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        f"DS exam,5,{effort},2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 2"):
        parse_csv(path)
