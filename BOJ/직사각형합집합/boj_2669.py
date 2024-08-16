''' # 26
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
'''
from pprint import pprint

def fill_one(x1, y1, x2, y2, arr): # 면적 채우기
    for x in range(x1, x2):
        for y in range(y1, y2):
            if arr != 1:
                arr[x][y] = 1

xy_axis = [[0] * 100 for _ in range(100)] # 좌표평면

for _ in range(4): # 채워넣는 과정
    x1, y1, x2, y2 = map(int, input().split())
    fill_one(x1, y1, x2, y2, xy_axis)

square = 0
for li in xy_axis: # 넓이 계산
    square += sum(li)

print(square)
