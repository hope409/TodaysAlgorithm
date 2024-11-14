from collections import defaultdict
col, row = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(col)]
blind = [[1] * row for _ in range(col)]
cctv = defaultdict(list)
for i in range(col):
    for j in range(row):
        if room[i][j]:
            cctv[room[i][j]].append((i, j))
print(cctv)
