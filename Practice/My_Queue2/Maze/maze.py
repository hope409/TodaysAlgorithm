vector_li = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(y, x):
    global result
    # 현재 위치가 도착점이라면
    # 목표점에 도달했거나 결과가 이미나와있다면 리턴
    if maze[y][x] == 3 or result:
        result = 1
        return
    for i, j in vector_li:
        d_y = y + i
        d_x = x + j
        # 반복하다가 결과가 나왔다면 리턴
        if result:
            return
        # 벽이 아니거나 왔던 위치가 아니라면
        if maze[d_y][d_x] != 1:
            # 현재위치를 벽으로 체크하고 재귀
            maze[y][x] = 1
            dfs(d_y, d_x)


t = 10
for test_case in range(1, t + 1):
    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    result = 0
    # 1,1 위치부터 탐색시작
    dfs(1, 1)
    print(f'#{tc} {result}')