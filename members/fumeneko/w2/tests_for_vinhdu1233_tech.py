import pytest

from members.vinhdu1233_tech.w1.grades import summary
from members.vinhdu1233_tech.w1.rules import can_register_thesis, missing
from members.vinhdu1233_tech.w1.text_tools import top_k
from members.vinhdu1233_tech.w1.timetable import by_day


def test_summary_grades():
    # Kiểm tra hàm tính toán điểm (W1-1)
    res = summary([7.0, 8.0, 9.0, 10.0])
    assert res['min'] == 7.0
    assert res['max'] == 10.0
    assert res['mean'] == 8.5
    assert res['median'] == 8.5

def test_summary_empty_exception():
    # Trường hợp biên: danh sách rỗng phải ném lỗi ValueError
    with pytest.raises(ValueError):
        summary([])

def test_text_tools_top_k():
    # Kiểm tra xử lý từ và đếm tần suất (W1-2)
    text = "Git is fun. Git is fast!"
    result = top_k(text, 2)
    assert result == [('git', 2), ('is', 2)]

def test_thesis_eligibility_success():
    # Kiểm tra điều kiện đủ đăng ký luận văn (W1-3)
    assert can_register_thesis(125, 2.5) == True

def test_thesis_eligibility_missing_reasons():
    # Kiểm tra trường hợp thiếu tín chỉ và GPA (W1-3)
    assert can_register_thesis(110, 1.8) == False
    reasons = missing(110, 1.8)
    assert isinstance(reasons, list)
    assert len(reasons) > 0

def test_timetable_grouping():
    # Kiểm tra nhóm thời khóa biểu theo ngày (W1-5)
    schedule = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
    grouped = by_day(schedule)
    assert grouped == {'Mon': ['CSC10001', 'CSC10014'], 'Tue': ['MTH00003']}
