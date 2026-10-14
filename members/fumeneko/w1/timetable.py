def by_day(schedule: list) -> dict:
    result = {}
    for code, day in schedule:
        if day not in result:
            result[day] = []
        result[day].append(code)
    for day, values in result.items():
        values.sort()
    return result