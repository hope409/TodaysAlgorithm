import sys
sys.stdin = open('sample_input.txt')

def f(i, j, bw, n):
    board[i][j] = bw
    for di, dj in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,1],[-1,0],[-1,-1]]:
        ni, nj = i + di, j + dj
        tmp = [] # 뒤집을 돌의 인덱스를 저장
        while 0 <= ni < n and 0 <= nj < n and board[ni][nj] == op[bw]:# 반대색 돌이면
            tmp.append((ni,nj)) # 뒤집을 돌을 저장
            ni, nj = ni + di, nj + dj
        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == bw:
            for p, q in tmp:
                board[p][q] = bw
# 1이면 흑돌, 2이면 백돌
B = 1
W = 2
op = [0, 2, 1]

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n, m = map(int, input().split()) # n : 보드의 크기 / m : 돌을 놓는 횟수
    play = [list(map(int, input().split())) for _ in range(m)] # 게임 진행

    board = [[0] * n for _ in range(n)] # 보드 만들기

    # 중심부 돌 배치
    # WB
    # BW 로 놓을 거임
    board[n // 2 - 1][n // 2 - 1] = W
    board[n // 2 - 1][n // 2] = B
    board[n // 2][n // 2 - 1] = B
    board[n // 2][n // 2] = W

    # 돌놓기
    for col, row, bw in play: # 입력 순서 주의
        f(row - 1,col - 1,bw,n) #좋기 뒤집기

    bcnt = wcnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1
    print(f"#{test_case} {bcnt} {wcnt}")