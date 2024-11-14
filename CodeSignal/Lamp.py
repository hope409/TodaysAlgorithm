def solution(lamps, points):
    length = len(points)
    answer = [0] * length
    for i in range(length):
        count = 0
        for lamp in lamps:
            if (lamp[0] - points[i]) * (lamp[1] - 1 - points[i]) <= 0:
                count += 1
        if count:
            answer[i] = count
    return answer

print(solution([[1, 3], [2, 5], [3, 7]], [3, 8, 9, 1]))