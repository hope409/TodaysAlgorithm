import sys
sys.stdin = open('input.txt')

def make_snail():
    pass

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 테스트케이스 시작
    n = int(input()) # 달팽이 크기
    snail_li = [[0] * n for _ in range(n)] # 달팽이 만들 공간
    # print(snail_li)
    vector_li = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 우 / 하 / 좌 / 상

    cnt = 1
    length = n
    col = 0
    row = 0
    rotation = 0
    while cnt != n**2:
        idx = rotation % 4
        vector = vector_li[idx]
        for i in range(length):
            col += vector[0]
            row += vector[1]
            cnt += 1
            snail_li[col][row] = cnt

        if idx % 2 == 1:
            length -= 1

        rotation += 1

    print(snail_li)
