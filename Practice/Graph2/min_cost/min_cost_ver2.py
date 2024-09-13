import sys
sys.stdin = open('sample_input.txt')

def move(end, start = 0, cost = 0):
    global min_cost
    if start == end:
        if min_cost is None or cost < min_cost:
            min_cost = cost
        return
    if min_cost is not None and cost >= min_cost:
        return

    for next in adj_li[start]:
        if visited[next]:
            continue
        if adj_li[start][next] <= 0:
            visited[next] = True
            move(end, next, cost + 1)
            visited[next] = False
        else:
            visited[next] = True
            move(end, next, cost + 1 + adj_li[start][next])
            visited[next] = False

t = int(input())
for test_case in range(1, t + 1):
    # 지도의 가로 세로 사이즈
    n = int(input())
    # 지도를 1차원 리스트로 펼쳐서 받아오기
    map_arr = sum([list(map(int, input().split())) for _ in range(n)], [])
    visited = [False] * (n * n)
    visited[0] = True

    # adj_li = [[x + i for i in [-3, -1, 1, 3]] for x in range(n*n)]
    # 인접 가중치 리스트 만들기
    adj_li = [{} for x in range(n*n)]
    for i in range(n * n):
        if i % n == 0:
            for k in [n, 1, -n]:
                if 0 <= i + k < n * n:
                    adj_li[i][i + k] = map_arr[i + k] - map_arr[i]
        elif i % n == n - 1:
            for k in [n, -1, -n]:
                if 0 <= i + k < n * n:
                    adj_li[i][i + k] = map_arr[i + k] - map_arr[i]
        else:
            for k in [n, 1, -1, -n]:
                if 0 <= i + k < n*n:
                    adj_li[i][i + k] = map_arr[i + k] - map_arr[i]
    min_cost = None
    move(n * n - 1)
    print(f"#{test_case} {min_cost}")