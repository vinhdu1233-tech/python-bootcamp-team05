def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}

    for course, day in schedule:
        if day not in result:
            result[day] = []

        result[day].append(course)

    for day in result:
        result[day].sort()

    return result


if __name__ == "__main__":
    print(by_day([
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon")
    ]))
