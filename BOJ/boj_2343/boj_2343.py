n, m = map(int, input().split())
lectures = list(map(int, input().split()))

# 최소 크기: 가장 긴 강의의 길이 (이보다 작으면 강의를 담을 수 없으므로)
# 최대 크기: 모든 강의를 한 블루레이에 담을 경우
left, right = max(lectures), sum(lectures)

# 이진 탐색을 통해 최소 블루레이 크기 찾기
while left < right:
    mid = (left + right) // 2
    count, current_sum = 1, 0  # 블루레이 수와 현재 블루레이의 합

    for lecture in lectures:
        if current_sum + lecture > mid:  # 현재 블루레이 크기를 초과하면 새로운 블루레이 시작
            count += 1
            current_sum = 0
        current_sum += lecture

    if count > m:  # 블루레이 수가 m을 초과하면 크기를 늘려야 함
        left = mid + 1
    else:  # 블루레이 수가 m 이하라면 크기를 줄일 수 있음
            right = mid
print(left)