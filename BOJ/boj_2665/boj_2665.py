'''
8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111
'''
from collections import deque
n = int(input())
maze = [list(map(int, input().strip())) for _ in range(n)]
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[n * n for _ in range(n)] for _ in range(n)] # 해당 위치까지 오는 경로들 중 흰색으로 바꾼 최소 횟수
visited[0][0] = 0 # 맨처음은 흰색으로 한번도 안바꿈 바꿈
queue = deque([[0, 0]]) # 처음 위치 세팅

while queue:
    y, x = queue.popleft()
    for dy, dx in delta:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n: # 범위가 유효한가?
            if maze[ny][nx]: # 흰색인가?
                if visited[y][x] < visited[ny][nx]: # 현재 위치에서 이동할 때가 더 최소인가?
                    visited[ny][nx] = visited[y][x] # 최소라면 갱신하고
                    queue.append([ny, nx]) # 다음 탐색을 위해 큐에 입력
            else: # 검은색인가?
                if visited[y][x] + 1 < visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append([ny, nx])
print(visited[n - 1][n - 1]) # 출구에서 최소값 출력