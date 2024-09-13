
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS():
    Q = deque()
    Q.append((0, 0))
    visited[0][0] = 0

    while Q:
        x, y = Q.popleft()
        for i in range(4):  # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]

            # 다음 좌표가 범위 내에 있고,
            # 목적지 좌표(N-1, N-1)의 방문 표시값보다 작거나 같은 경우에만 진행
            # WHY ? 더 크다면, 이미 더 작은 값으로 방문했기 때문에 더 이상 진행할 필요가 없음
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] <= visited[N - 1][N - 1]:
                if data[x][y] >= data[nx][ny]:  # 다음 칸의 높이가 현재 칸의 높이보다 작거나 같은 경우
                    if visited[nx][ny] > visited[x][y] + 1: # 다음 위치 방문 표시값이 현재 위치 방문 표시값 + 1보다 큰 경우 즉, 더 작은 값으로 방문할 수 있는 경우
                        # 다음 칸의 방문 표시값을 현재 칸의 방문 표시값 + 1로 업데이트
                        visited[nx][ny] = visited[x][y] + 1  # 다음 칸의 방문 표시값을 현재 칸의 방문 표시값 + 1로 업데이트, 낮거나 같은 곳임으로 1만큼의 연료가 들고 이동
                        Q.append((nx, ny))  # 다음 칸을 큐에 추가
                # 인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고, 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.
                elif data[x][y] < data[nx][ny]:  # 현재 칸의 높이가 다음 칸의 높이보다 작은 경우(높은곳으로 이동)
                    # 다음 칸의 높이가 현재 칸의 높이보다 큰 경우
                    if visited[nx][ny] > visited[x][y] + 1 + (data[nx][ny] - data[x][y]):
                        # 다음 칸의 방문 표시값을 현재 칸의 방문 표시값 + 1 + (다음 칸의 높이 - 현재 칸의 높이)로 업데이트
                        visited[nx][ny] = visited[x][y] + 1 + (data[nx][ny] - data[x][y])
                        Q.append((nx, ny))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    min_num = sum(sum(data, [])) + N + 1
    visited = [[min_num for _ in range(N)] for _ in range(N)]

    BFS()
    print(f'#{tc} {visited[N - 1][N - 1]}')
