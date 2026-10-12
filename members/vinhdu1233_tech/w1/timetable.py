
def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and sort course names alphabetically."""

    timetable = {}

    for course, day in entries:
        timetable.setdefault(day, []).append(course)

    for courses in timetable.values():
        courses.sort()

    return timetable
