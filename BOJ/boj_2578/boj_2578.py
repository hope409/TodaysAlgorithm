from pprint import pprint
board1 = [list(map(int, input().split())) for _ in range(5)] # 입력받기
board2 = [[0] * 5 for _ in range(5)] # 전치행렬
for i in range(5): # 전치행렬 만들기
    for j in range(5):
        board2[i][j] = board1[j][i]
number_li = []
for _ in range(5):
    number_li += list(map(int, input().split()))

cnt = -1
bingo_li = [[0,0,0,0,0], [0,0,0,0,0], [0,0]] # 가로 세로 대각
while True:
    cnt += 1
    if cnt == 25:
        break
    number = number_li[cnt]
    for i in range(5):
        for j in range(5):
            if board1[i][j] == number:
                board1[i][j] = 0
                board2[j][i] = 0
    if cnt > 11:
        cross1 = 0
        cross2 = 0
        for axis in range(3):
            for idx in bingo_li[axis]:
                if axis == 0:
                    if idx == 0 and sum(board1[idx]) == 0:
                        bingo_li[idx] = 1
                elif axis == 1:
                    if idx == 0 and sum(board2[idx]) == 0:
                        bingo_li[idx] = 1
                elif axis == 2:
                    if idx == 0:
                        for k in range(5):
                            cross1 += board1[k][k]
                            cross2 += board1[k][4 - k]
                            if cross1 == 0:
                                bingo_li[2][0] = 1
                            if cross2 == 0:
                                bingo_li[2][1] = 1

    if sum(bingo_li[0]) + sum(bingo_li[1]) + sum(bingo_li[2]) >= 3:
        print(cnt + 1)
        break