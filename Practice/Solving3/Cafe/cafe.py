import sys
sys.stdin = open('sample_input.txt')

direction = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
path = []
def find_route(n, x, y, idx = 0, cnt = 0): # 길찾기
    global max_cnt
    if cnt == 3:
        if n * x + y == path[0] and len(path) > max_cnt:
            max_cnt = len(path)
        return
    for i in range(2):
        if cnt == 3:
            if i:
                return
        dx, dy = direction[idx + i]
        if visited[x][y] or count_arr[cafe_arr[x][y]]:
            continue
        if 0 <= x + dx < n and 0 <= y + dy < n:
            visited[x][y] = True
            count_arr[cafe_arr[x][y]] += 1
            path.append(n * x + y)
            if i:
                find_route(n, x + dx, y + dy, idx + i, cnt + 1)
            else:
                find_route(n, x + dx, y + dy, idx + i, cnt)
            path.pop()
            count_arr[cafe_arr[x][y]] -= 1
            visited[x][y] = False

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n = int(input()) # 카페의 크기
    visited = [[False] * n for _ in range(n)]
    count_arr = [0] * 101 # 디저트의 개수
    cafe_arr = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    for i in range((n + 1) // 2):
        for j in range(1, 1 + (n + 1) // 2):
            find_route(n, i, j)

    if max_cnt:
        print(f"#{test_case} {max_cnt}")

    else:
        print(f"#{test_case} -1")