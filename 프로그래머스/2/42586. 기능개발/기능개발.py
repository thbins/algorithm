def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        days.append((100 - p + s - 1) // s)

    result = []
    leader = days[0]
    count = 1

    for d in days[1:]:
        if d <= leader:
            count += 1
        else:
            result.append(count)
            leader = d
            count = 1

    result.append(count)
    return result