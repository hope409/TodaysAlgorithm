import sys
from pprint import pprint
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n = int(input()) # 미로의 크기
    maze = [list(map(int, input())) for _ in range(n)] # 미로 받아오기
    s, g = -1, -1 # s : 출발노드 / g : 도착노드
    for col in range(n): # 출발, 도착노드 찾기
        for row in range(n):
            if maze[col][row] == 2:
                s = [col, row]
                if g != -1:
                    break
            elif maze[col][row] == 3:
                g = [col, row]
                if s != -1:
                    break
    # print(s, g)
    col, row = s #
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append([col, row])
    status = False
    while q and not status:
        # print(q)
        col, row = q.pop(0)
        # pprint(visited)
        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]: # 상우하좌 탐색
            if 0 <= col + dx < n and 0 <= row + dy < n: # 미로 안에서만 탐색
                if maze[col + dx][row + dy] == 0 and visited[col + dx][row + dy] == 0:
                    q.append([col + dx, row + dy])
                    visited[col + dx][row + dy] = visited[col][row] + 1
                elif maze[col + dx][row + dy] == 3:
                    status = True
                    break
    if status == True:
        print(f"#{test_case} {visited[col][row]}")
    else:
        print(f"#{test_case} 0")

