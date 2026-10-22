try:
    from .io_utils import load_tasks, save_json
except ImportError:
    from io_utils import load_tasks, save_json

tasks = load_tasks("members/lnmthi/w2/task.csv")

for task in tasks:
    print(task)

save_json(tasks, "members/lnmthi/w2/tasks.json")
print("CSV loaded and JSON saved!")


try:
    from .errors import InfeasiblePlan, check_feasible
except ImportError:
    from errors import InfeasiblePlan, check_feasible
try:
    check_feasible(tasks, 2.0)
except InfeasiblePlan as error:
    print("Caught infeasible plan:", error)
