from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def test_sample_csv_runs_through_study_planner_pipeline():
    sample_csv = (
        Path(__file__).resolve().parents[1]
        / "shared"
        / "study_planner"
        / "sample_tasks.csv"
    )

    tasks = parse_csv(sample_csv)
    ordered_tasks = prioritise(tasks, today=date(2026, 10, 20))
    blocks = allocate(ordered_tasks, hours=12.0)
    result = render(blocks)

    assert len(tasks) == 4
    assert sum(block.hours for block in blocks) == 12.0
    assert result == (
        "Review Python: 2 hours\n"
        "Complete assignment: 3.5 hours\n"
        "Prepare for exam: 5 hours\n"
        "Practice algorithms: 1.5 hours"
    )
