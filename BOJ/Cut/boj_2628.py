''' # 30
10 8
3
0 3
1 4
0 2
'''

width, height = map(int, input().split()) # 가로 세로
n = int(input()) # 점선의 수
axis_0 = [0, height]
axis_1 = [0, width]
for _ in range(n):
    axis, idx = map(int, input().split())
    if axis == 0:
        axis_0.append(idx)
    else:
        axis_1.append(idx)

axis_1.sort()
axis_0.sort()
max_square = 0
for i in range(len(axis_1) - 1):
    for j in range(len(axis_0) - 1):
        pre_square = (axis_1[i + 1] - axis_1[i]) * (axis_0[j + 1] - axis_0[j])
        if pre_square > max_square:
            max_square = pre_square
print(max_square)