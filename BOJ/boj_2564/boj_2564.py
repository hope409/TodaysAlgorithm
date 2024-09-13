x, y = map(int, input().split())
n = int(input())
position_li = [list(map(int, input().split())) for _ in range(n + 1)]
axis_li = [[] for _ in range(n + 1)]
for i in range(n + 1):
    if position_li[i][0] == 1:
        axis_li[i] = [0, position_li[i][1]]
    elif position_li[i][0] == 2:
        axis_li[i] = [y, position_li[i][1]]
    elif position_li[i][0] == 3:
        axis_li[i] = [position_li[i][1], 0]
    elif position_li[i][0] == 4:
        axis_li[i] = [position_li[i][1], y]
