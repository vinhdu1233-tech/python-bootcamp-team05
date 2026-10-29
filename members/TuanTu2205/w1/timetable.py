def by_day(items: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by weekday and sort course names alphabetically."""
    timetable: dict[str, list[str]] = {}

    for course, day in items:
        timetable.setdefault(day, []).append(course)

    for courses in timetable.values():
        courses.sort()

    return timetable
