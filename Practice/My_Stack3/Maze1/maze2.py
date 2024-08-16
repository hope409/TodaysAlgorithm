import sys
sys.stdin = open('sample_input.txt')
'''
또 다른 방법
for dx, dy in [(-1, 0), (1, 0)]:
'''

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y):
    stack = [(x, y)] # 스택 초기화
    visited[x][y] = 1
    # 언제까지 탐색을 할건가요?
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로의 범위를 벗어나지 않는지 &&
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] != 1 and visited[nx][ny] != 1:
                if maze[nx][ny] == 3: # 다음 위치가 출구이다.
                    return 1 # 1 반환 후 함수 종료
                # 3이 아니라면
                stack.append((nx, ny))
                visited[nx][ny] = 1
    return 0

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())

    maze = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    # 2가 담긴 곳 == 출발점
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                print(f"#{test_case} {search(i, j)}")