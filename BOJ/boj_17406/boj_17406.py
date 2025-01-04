from copy import deepcopy
from itertools import permutations


def rotate_matrix(arr, r, c, s):
    # s만큼의 반지름으로 회전
    # 중심은 r, c
    start_r, start_c = r - 1, c - 1

    for layer in range(1, s + 1):
        top = start_r - layer
        bottom = start_r + layer
        left = start_c - layer
        right = start_c + layer

        # 테두리를 회전
        # 위쪽 변
        for i in range(right, left, -1):
            arr[top][i] = arr[top][i - 1]

    min_temp_arr = min(sum(li) for li in arr)

    return min_temp_arr


n, m, k = map(int, input().split()) # 배열의 크기, 회전 연산 개수
array = [list(map(int, input().split())) for _ in range(n)]
rotations = [list(map(int, input().split())) for _ in range(k)]

min_array = None # 최소값을 저장할 변수

rotations_li = list(permutations(range(0, k)))

for li in rotations_li:
    for idx in li:
        r, c, s = rotations[idx]
        temp_arr = deepcopy(array)
        temp_min = rotate_matrix(temp_arr, r, c, s)
    if min_array
    min_array = min(min_array, temp_min)