direction = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 하 우 상 좌

def move(n, m, x = 0, y = 0, cnt = 1):
    global min_cnt
    if x == n - 1 and y == m - 1:
        if min_cnt is None or cnt < min_cnt:
            min_cnt = cnt
        return
    if route[x][y] < cnt:
        return
    # if min_cnt is not None and cnt >= min_cnt:
    #     return

    for dx, dy in direction:
        if min_cnt is not None:
            return
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze_arr[nx][ny]:
            visited[nx][ny] = True
            route[nx][ny] = cnt + 1
            move(n, m, nx, ny, cnt + 1)
            visited[nx][ny] = False


n, m = map(int, input().split()) # n : 세로 / m : 가로
maze_arr = [[int(x) for x in input()] for _ in range(n)]
visited = [[False] * m for _ in range(n)]
route = [[m*n] * m for _ in range(n)] # 해당 위치까지 오는 가장 최소경로길이
min_cnt = None
visited[0][0] = True
route[0][0] = 1
move(n, m)
print(min_cnt)