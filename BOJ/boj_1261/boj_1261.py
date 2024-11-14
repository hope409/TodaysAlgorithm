'''
3 3
011
111
110
'''
from collections import deque
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
m, n = map(int, input().split()) # 가로세로
map_arr = [list(map(int, input())) for _ in range(n)]
first = (0, 0, 0, set()) # 초기좌표, 부순벽, 방문기록
queue = deque([first])
min_bomb = m * n
while queue:
    y, x, bomb, visited = queue.popleft()
    if y == n - 1 and x == m - 1:
        min_bomb = min(min_bomb, bomb)
        continue
    if bomb >= min_bomb:
        continue
    visited = visited.copy()
    visited.add((y, x))
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if (ny, nx) in visited:
                continue
            if map_arr[ny][nx]:
                queue.append((ny, nx, bomb + 1, visited))
            else:
                queue.append((ny, nx, bomb, visited))
print(min_bomb)