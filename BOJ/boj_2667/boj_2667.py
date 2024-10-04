'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
n = int(input())
map_list = [list(map(lambda x : int(x), list(input()))) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
stack = []
apart = []
for i in range(n):
    for j in range(n):
        if map_list[i][j] and not visited[i][j]:
            stack.append((i, j))
            count = 0
            while stack:
                y, x = stack.pop()
                if visited[y][x]:
                    continue
                visited[y][x] = True
                count += 1
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n and map_list[ny][nx] and not visited[ny][nx]:
                        stack.append((ny, nx))
            apart.append(count)
apart.sort()
print(len(apart))
for x in apart:
    print(x)