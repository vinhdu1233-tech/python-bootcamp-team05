def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits, gpa) -> list[str]:
    min_credits = 120
    min_gpa = 2.0
    lst_string = []
    if credits < min_credits:
        lst_string.append(f"need {min_credits - credits} more credit(s)")
    if gpa < min_gpa:
        lst_string.append(f"need {min_gpa - gpa} more gpa")
    if not lst_string:
        lst_string.append("No missing requirment")
    return lst_string

if __name__ == "__main__":
    print(can_register_thesis(140, 3.0))
    print(missing(10, 3.0))