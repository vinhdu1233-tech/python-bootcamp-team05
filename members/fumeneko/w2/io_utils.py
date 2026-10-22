import csv
import json
from datetime import date

from .models import Task  # Giả sử Task được import từ models.py trong cùng gói


def load_tasks(path: str) -> list[Task]:
    """Đọc danh sách Task từ file CSV. Ném ValueError kèm số dòng nếu dữ liệu lỗi."""
    tasks = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # Bắt đầu từ dòng 2 (vì dòng 1 là header)
        for line_num, row in enumerate(reader, start=2):
            try:
                title = row['title'].strip()
                importance = int(row['importance'])
                effort_h = float(row['effort_h'])
                deadline = date.fromisoformat(row['deadline'].strip())
                
                task = Task(title=title, importance=importance, effort_h=effort_h, deadline=deadline)
                tasks.append(task)
            except (ValueError, KeyError, AttributeError) as e:
                raise ValueError(f"Invalid row at line {line_num}: {e}")
                
    return tasks

def save_json(tasks: list[Task], path: str) -> None:
    """Lưu danh sách Task ra file JSON."""
    data = []
    for t in tasks:
        data.append({
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat()  # Chuyển date thành chuỗi 'YYYY-MM-DD'
        })
    
    with open(path, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)