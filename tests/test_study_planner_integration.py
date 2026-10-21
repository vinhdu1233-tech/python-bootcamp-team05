from datetime import date, timedelta

from shared.contract import Task

# Import your team's modules once merged to main:
# from shared.study_planner.parse import parse_csv
# from shared.study_planner.prioritise import prioritise
# from shared.study_planner.allocate import allocate
# from shared.study_planner.render import render

def test_pipeline_empty_csv(tmp_path):
    # Test handling of empty or missing records
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("title,importance,effort_h,deadline\n")
    # Add assertions matching your implementation behavior

def test_pipeline_overdue_and_zero_hours():
    # Test task prioritization with overdue tasks and zero available hours allocation
    today = date.today()
    Task(title="Old Task", importance=5, effort_h=2.0, deadline=today - timedelta(days=2))
    # Run integration checks
