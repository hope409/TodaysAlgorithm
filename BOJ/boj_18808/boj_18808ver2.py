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

# 스티커를 시계방향으로 회전하는 함수
def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(e) for e in list_of_tuples]


# 노트북에 스티커를 부착하는 함수
def attach(i, j, r, c, sticker):
    for x in range(r):
        for y in range(c):
            if sticker[x][y] == 1:
                notebook[i + x][j + y] = 1

n, m, k = map(int, input().split()) # 세로 / 가로 / 스터커의 개수
notebook = [[0] * m for _ in range(n)]
# print(notebook)
for _ in range(k):
    r, c = map(int, input().split()) # 스티커의 행과 열의 개수
    sticker = [list(map(int, input().split())) for _ in range(r)]
    is_attach = False
    for rotate in range(4):
        r, c = len(sticker), len(sticker[0])
        if is_attach: # 이미 스티커를 부착했다면?
            break
        if r > n or c > m:  # 스티커가 노트북보다 크다면?
            continue
        for i in range(n - r + 1):
            for j in range(m - c + 1):
                if all(
                        notebook[i + x][j + y] * sticker[x][y] == 0
                        for x in range(r)
                        for y in range(c)
                ):
                    attach(i, j, r, c, sticker)  # 스티커를 노트북에 부착
                    is_attach = True
                    break
            if is_attach: # 이미 스티커를 부착했다면?
                break
        sticker = rotated(sticker)
        pprint(sticker)

pprint(notebook)
print(sum(sum(notebook, [])))