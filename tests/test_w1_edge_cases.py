```python
"""Week 1 edge-case tests for all 6 team members.

These are additional student-written tests.
Update function names and expected outputs to match each member's implementation.
"""

import importlib.util
from pathlib import Path

import pytest


PROJECT_DIR = Path(__file__).resolve().parents[1]
MEMBERS_DIR = PROJECT_DIR / "members"


def load_module(member, filename):
    """Load a Python module from a member's w1 directory."""
    path = MEMBERS_DIR / member / "w1" / f"{filename}.py"

    if not path.exists():
        pytest.fail(f"Exercise file not found: {path}")

    spec = importlib.util.spec_from_file_location(
        f"{member}_{filename}", path
    )
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ============================================================
# Variant 1: vinhdu1233_tech
# Expected exercises: grades, text_tools, rules, translate,
#                     timetable
# ============================================================

def test_v1_grades_single_score():
    grades = load_module("vinhdu1233_tech", "grades")
    result = grades.summary([8])

    assert result["min"] == 8
    assert result["max"] == 8
    assert result["mean"] == 8
    assert result["median"] == 8


def test_v1_grades_empty_list():
    grades = load_module("vinhdu1233_tech", "grades")

    with pytest.raises(ValueError):
        grades.summary([])


def test_v1_word_count_empty_text():
    text_tools = load_module("vinhdu1233_tech", "text_tools")

    assert text_tools.word_count("") == 0


def test_v1_word_count_mixed_case():
    text_tools = load_module("vinhdu1233_tech", "text_tools")

    assert text_tools.word_count("Python python PYTHON") == 3


def test_v1_thesis_exact_threshold():
    rules = load_module("vinhdu1233_tech", "rules")

    assert rules.can_register_thesis(120, 2.0)


def test_v1_binary_search_empty_list():
    translate = load_module("vinhdu1233_tech", "translate")

    assert translate.binary_search([], 5) == -1


def test_v1_timetable_empty_list():
    timetable = load_module("vinhdu1233_tech", "timetable")

    assert timetable.by_day([]) == {}


# ============================================================
# Variant 2: TuanTu2205
# TODO: Replace the example module/function names with the
# actual Week 1 exercises assigned to this member.
# ============================================================

def test_v2_empty_input():
    pytest.skip(
        "Add edge-case assertions after confirming TuanTu2205's "
        "module and function names."
    )


def test_v2_single_item_input():
    pytest.skip(
        "Add a single-item input test for TuanTu2205's exercise."
    )


# ============================================================
# Variant 3: tree312_coder
# ============================================================

def test_v3_empty_input():
    pytest.skip(
        "Add edge-case assertions after confirming tree312_coder's "
        "module and function names."
    )


def test_v3_boundary_input():
    pytest.skip(
        "Add a boundary-value test for tree312_coder's exercise."
    )


# ============================================================
# Variant 4: dmdung2520
# ============================================================

def test_v4_empty_input():
    pytest.skip(
        "Add edge-case assertions after confirming dmdung2520's "
        "module and function names."
    )


def test_v4_boundary_input():
    pytest.skip(
        "Add a boundary-value test for dmdung2520's exercise."
    )


# ============================================================
# Variant 5: fumeneko
# ============================================================

def test_v5_empty_input():
    pytest.skip(
        "Add edge-case assertions after confirming fumeneko's "
        "module and function names."
    )


def test_v5_boundary_input():
    pytest.skip(
        "Add a boundary-value test for fumeneko's exercise."
    )


# ============================================================
# Variant 6: lnmthi
# ============================================================

def test_v6_empty_input():
    pytest.skip(
        "Add edge-case assertions after confirming lnmthi's "
        "module and function names."
    )


def test_v6_boundary_input():
    pytest.skip(
        "Add a boundary-value test for lnmthi's exercise."
    )
```
