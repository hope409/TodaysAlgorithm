import sys
sys.stdin = open('sample_input.txt')

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def find(y, x, height, length = 1, used = False):
    global max_length
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n:
            next_height = map_info[ny][nx]
            if next_height < height:
                pre_length = find(ny, nx, next_height, length + 1)
            elif not used:
                for h in range(1, k + 1):
                    pre_length = find(ny, nx, next_height - h, length + 1, True)
    if pre_length > max_length:
        max_length = pre_length

t = int(input())
for test_case in range(1, t + 1):
    n, k = map(int, input().split()) # n : 한변의 길이 / k : 최대 공사 가능 깊이
    map_info = [list(map(int, input().split())) for _ in range(n)] # 지도의 정보
    map_info2 = sum(map_info, [])
    peak_info = [i for i, value in enumerate(map_info2) if value == max(map_info2)]
    # print(peak_info)
    max_length = 0
    used = False
    for peak in peak_info:
        y, x = peak // n, peak % n
        peak_height = map_info[y][x]
        find(y, x, peak_height)

    print(max_length)