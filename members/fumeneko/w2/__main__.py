from pathlib import Path

from .io_utils import load_tasks


def main():
    sample_path = Path("samples/tasks.csv")
    
    if not sample_path.exists():
        print(f"[Error] Không tìm thấy file mẫu tại đường dẫn: {sample_path}")
        return

    try:
        print(f"Đang tải dữ liệu từ {sample_path}...")
        tasks = load_tasks(sample_path)
        
        print(f"Thành công! Đã tải {len(tasks)} task(s):")
        for idx, t in enumerate(tasks, start=1):
            print(f"  {idx}. {t.title} | Độ quan trọng: {t.importance} | Thời gian: {t.effort_h}h | Hạn chót: {t.deadline}")
            
    except ValueError as e:
        print(f"[Data Error] Lỗi định dạng dữ liệu: {e}")
    except Exception as e:  # noqa: BLE001
        print(f"[Unexpected Error] Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()