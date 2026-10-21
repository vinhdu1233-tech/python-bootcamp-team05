from io_utils import load_tasks, save_json

tasks = load_tasks("members/lnmthi/w2/task.csv")

for task in tasks:
    print(task)

save_json(tasks, "members/lnmthi/w2/tasks.json")
print("CSV loaded and JSON saved!")


from errors import check_feasible, InfeasiblePlan

try:
    check_feasible(tasks, 2.0)
except InfeasiblePlan as error:
    print("Caught infeasible plan:", error)
