import sys
sys.stdin = open('sample_input.txt')

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 하 우 상 좌

def move_cost(end_x, end_y, cost = 0, start_x = 0, start_y = 0):
    global min_cost
    if start_x == end_x - 1 and start_y == end_y - 1:
        if min_cost is None or cost < min_cost:
            min_cost = cost
        return
    if min_cost is not None and cost >= min_cost:
        return
    visited[start_x][start_y] = True
    for dx, dy in direction:
        nx, ny = start_x + dx, start_y + dy
        if 0 <= nx < end_x and 0 <= ny < end_y and not visited[nx][ny]:
            add_cost = map_arr[nx][ny] - map_arr[start_x][start_y]
            if add_cost < 0:
                add_cost = 0
            move_cost(end_x, end_y, cost + 1 + add_cost, nx, ny)
    visited[start_x][start_y] = False

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    map_arr = [list(map(int, input().split())) for _ in range(n)]
    min_cost = None
    visited = [[False] * n for _ in range(n)]
    move_cost(n, n)
    print(f"#{test_case} {min_cost}")