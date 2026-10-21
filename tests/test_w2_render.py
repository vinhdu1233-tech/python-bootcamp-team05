from datetime import date

from shared.contract import Block, Task

task = Task(
    title="Python",
    importance=3,
    effort_h=2.5,
    deadline=date(2026, 10, 22),
)

block = Block(task=task, hours=1.5)