class InfeasiblePlan(Exception):
    """Ngoại lệ được ném ra khi tổng thời gian thực hiện các task vượt quá thời gian có sẵn."""
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"Plan is infeasible: needed {needed_h}h, but only {available_h}h available.")

def check_feasible(tasks, available_h: float) -> None:
    """Kiểm tra xem tổng số giờ của các task có vượt quá giờ có sẵn không."""
    total_needed = sum(task.effort_h for task in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)