
def group_by_day(timetable: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}

    for entry in timetable:
        day = entry["day"]
        grouped.setdefault(day, []).append(entry)

    return grouped


if __name__ == "__main__":
    timetable = [
        {"day": "Monday", "subject": "Python"},
        {"day": "Tuesday", "subject": "Math"},
        {"day": "Monday", "subject": "Database"},
    ]

    print(group_by_day(timetable))
