from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render


def make_block(title: str, hours: float) -> Block:
    task = Task(
        title=title,
        importance=3,
        effort_h=4.0,
        deadline=date(2026, 10, 22),
    )
    return Block(task=task, hours=hours)


def test_render_multiple_blocks():
    blocks = [
        make_block("Python", 1.5),
        make_block("C++", 2.0),
    ]

    result = render(blocks)

    assert result == (
        "Python: 1.5 hours\n"
        "C++: 2 hours"
    )


def test_render_empty_list():
    assert render([]) == ""


def test_render_fractional_hours():
    blocks = [make_block("Python", 1.5)]

    assert render(blocks) == "Python: 1.5 hours"


def test_render_zero_hours():
    blocks = [make_block("Review", 0)]

    assert render(blocks) == "Review: 0 hours"


def test_render_integer_hours_without_decimal():
    blocks = [make_block("Algorithms", 3.0)]

    assert render(blocks) == "Algorithms: 3 hours"
