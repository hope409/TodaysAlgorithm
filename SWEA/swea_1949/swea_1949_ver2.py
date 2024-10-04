import sys
sys.stdin = open('sample_input.txt')

from collections import deque
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

t = int(input())
for test_case in range(1, t + 1):
    n, k = map(int, input().split()) # n : 한변의 길이 / k : 최대 공사 가능 깊이
    map_info = [list(map(int, input().split())) for _ in range(n)] # 지도의 정보
    map_info2 = sum(map_info, [])
    max_height = max(map_info2)
    peak_info = [i for i, value in enumerate(map_info2) if value == max_height]
    max_length = 0
    for peak in peak_info:
        pre_length = 1
        used = False
        start_peak = [peak // n, peak % n, max_height, pre_length, [], used]
        queue = deque([start_peak])
        while queue:
            y, x, pre_height, pre_length, visited, used = queue.popleft()
            visited = visited.copy()
            visited.append(n * y + x)
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n and n * ny + nx not in visited:
                    if map_info[ny][nx] < pre_height:
                        queue.append([ny, nx, map_info[ny][nx], pre_length + 1, visited, used])
                    elif not used:
                        for sub_height in range(1, k + 1):
                            if map_info[ny][nx] - sub_height < pre_height:
                                queue.append([ny, nx, map_info[ny][nx] - sub_height, pre_length + 1, visited, True])
        if pre_length > max_length:
            max_length = pre_length
    print(f"#{test_case} {max_length}")
