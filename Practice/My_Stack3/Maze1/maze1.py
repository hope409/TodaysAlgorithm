import sys
from pprint import pprint
sys.stdin = open('sample_input.txt')

def find_point(x, n): # x : 찾을 포인트 / n : 미로의 크기 / arr : 미로
    for i in range(n):
        for j in range(n):
            if maze_arr[i][j] == x: # 찾은 경우
                return i, j
    return None, None # 못찾은 경우

# def find_goal(col, row, n):
#     if result == 1:
#         return
#     for i, j in vector_li:
#         # pprint(maze_arr)
#         if 0 <= col + i < n and 0 <= row + i < n and maze_arr[col + i][row + j] != 1:
#             if maze_arr[col + i][row + j] == 3:
#                 result = 1
#             if maze_arr[col + i][row + j] == 0:
#                 maze_arr[col][row] = 1
#                 find_goal(col + i, row + j, n)
#             # elif maze_arr[col + i][row + j] == 4:
#             #     maze_arr[col][row] = 1
#             #     find_goal(col + i, row + j, n)

def find_goal2(col, row, n):
    for i, j in vector_li:
        # pprint(maze_arr)
        if 0 <= col + i < n and 0 <= row + i < n and maze_arr[col + i][row + j] != 1:
            if maze_arr[col + i][row + j] == 3:
                return col + i, col + j, 1
            if maze_arr[col + i][row + j] == 0:
                maze_arr[col][row] = 4
                return col + i, col + j, 0
            elif maze_arr[col + i][row + j] == 4:
                maze_arr[col][row] = 1
                return col + i, col + j, 0



t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 미로의 크기
    maze_arr = [list(map(int, input())) for _ in range(n)] # 미로 입력
    # pprint(mage_arr)
    vector_li = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 우하좌상 : 시계방향순
    start_i, start_j = find_point(2, n)
    status = 0
    while status != 1:
        start_i, start_j, status = find_goal2(start_i, start_j, n)

    print(status)
