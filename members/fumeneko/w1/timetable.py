def by_day(schedule: list) -> dict:
    result = {}
    for code, day in schedule:
        if day not in result:
            result[day] = []
        result[day].append(code)
    for day in result:
        result[day].sort()
    return result
