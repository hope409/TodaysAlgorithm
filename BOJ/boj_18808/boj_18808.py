'''
5 4 4
3 3
1 0 1
1 1 1
1 0 1
2 5
1 1 1 1 1
0 0 0 1 0
2 3
1 1 1
1 0 1
3 3
1 0 0
1 1 1
1 0 0
'''

from pprint import pprint

# 노트북에 스티커를 부착하는 함수
def attach(i, j, r, c, sticker, rotate):
    for x in range(r):
        for y in range(c):
            if rotate == 0:  # 0도 회전
                if sticker[x][y] == 1:
                    notebook[i + x][j + y] = 1
            elif rotate == 1:  # 90도 회전
                if sticker[r - y - 1][x] == 1:
                    notebook[i + x][j + y] = 1
            elif rotate == 2:  # 180도 회전
                if sticker[r - x - 1][c - y - 1] == 1:
                    notebook[i + x][j + y] = 1
            elif rotate == 3:  # 270도 회전
                if sticker[y][c - x - 1] == 1:
                    notebook[i + x][j + y] = 1
    # pprint(notebook)

n, m, k = map(int, input().split()) # 세로 / 가로 / 스터커의 개수
notebook = [[0] * m for _ in range(n)]
# print(notebook)
for _ in range(k):
    r, c = map(int, input().split()) # 스티커의 행과 열의 개수
    sticker = [list(map(int, input().split())) for _ in range(r)]
    is_attach = False
    for rotate in range(4):
        if is_attach: # 이미 스티커를 부착했다면?
            break
        if rotate == 0: # 0도
            if r > n or c > m:  # 스티커가 노트북보다 크다면?
                continue
            for i in range(n - r + 1):
                for j in range(m - c + 1):
                    if all(
                            notebook[i + x][j + y] * sticker[x][y] == 0
                            for x in range(r)
                            for y in range(c)
                    ):
                        attach(i, j, r, c, sticker, rotate)  # 스티커를 노트북에 부착
                        is_attach = True
                        break
                if is_attach: # 이미 스티커를 부착했다면?
                    break

        elif rotate == 1: # 90도
            if r > m or c > n:  # 스티커가 노트북보다 크다면?
                continue
            for i in range(n - c + 1):
                for j in range(m - r + 1):
                    if all(
                            notebook[i + x][j + y] * sticker[r - y - 1][x] == 0
                            for x in range(c)
                            for y in range(r)
                    ):
                        attach(i, j, r, c, sticker, rotate)  # 스티커를 노트북에 부착
                        is_attach = True
                if is_attach:
                    break

        elif rotate == 2: # 180도
            if r > n or c > m:  # 스티커가 노트북보다 크다면?
                continue
            for i in range(n - r + 1):
                for j in range(m - c + 1):
                    if all(
                            notebook[i + x][j + y] * sticker[r - x - 1][c - y - 1] == 0
                            for x in range(r)
                            for y in range(c)
                    ):
                        attach(i, j, r, c, sticker, rotate)  # 스티커를 노트북에 부착
                        is_attach = True
                if is_attach:
                    break

        elif rotate == 3: # 270도
            if r > m or c > n:  # 스티커가 노트북보다 크다면?
                continue
            for i in range(n - c + 1):
                for j in range(m - r + 1):
                    if all(
                            notebook[i + x][j + y] * sticker[y][c - x - 1] == 0
                            for x in range(c)
                            for y in range(r)
                    ):
                        attach(i, j, r, c, sticker, rotate)  # 스티커를 노트북에 부착
                        is_attach = True
                if is_attach:
                    break

pprint(notebook)
print(sum(sum(notebook, [])))