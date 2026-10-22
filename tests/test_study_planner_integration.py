from datetime import date, timedelta

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def test_pipeline_empty_csv(tmp_path):
    # Test xử lý file CSV rỗng (chỉ có header)
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("title,importance,effort_h,deadline\n", encoding="utf-8")
    
    tasks = parse_csv(str(csv_file))
    assert len(tasks) == 0

    today = date.today()
    prioritized = prioritise(tasks, today)
    assert len(prioritized) == 0

    blocks = allocate(prioritized, available_hours=5.0)
    assert len(blocks) == 0

    output = render(blocks)
    assert isinstance(output, str)

def test_pipeline_overdue_and_zero_hours(tmp_path):
    # Test task quá hạn và cấp phát 0 giờ
    csv_file = tmp_path / "tasks.csv"
    today = date.today()
    overdue_deadline = today - timedelta(days=2)
    
    csv_file.write_text(
        f"title,importance,effort_h,deadline\n"
        f"Old Task,5,2.0,{overdue_deadline.isoformat()}\n",
        encoding="utf-8"
    )
    
    tasks = parse_csv(str(csv_file))
    assert len(tasks) == 1
    assert tasks[0].title == "Old Task"

    prioritized = prioritise(tasks, today)
    assert len(prioritized) == 1

    # Thử nghiệm với available_hours = 0.0
    blocks = allocate(prioritized, available_hours=0.0)
    assert len(blocks) == 0

    # Thử nghiệm với available_hours đủ thời gian
    blocks_allocated = allocate(prioritized, available_hours=5.0)
    assert len(blocks_allocated) == 1
    assert blocks_allocated[0].task.title == "Old Task"

    output = render(blocks_allocated)
    assert "Old Task" in output