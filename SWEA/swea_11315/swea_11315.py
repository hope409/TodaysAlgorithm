import sys
sys.stdin = open('sample_input.txt')

di = [0, 1, 1, 1] # 아래, 오른쪽대각선, 오른쪽, 왼쪽대각선
dj = [1, 1, 0, -1]
def f(n):
    for i in range(n):
        for j in range(n):
            for k in range(4):
                cnt = 0
                ni, nj = i, j # 돌인지 확인할 위치
                while 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                    ni += di[k]
                    nj += dj[k]
    return 'NO' # 연속한 5개를 못찾았을 때


t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n = int(input()) # 보드의 크기
    board = [input() for _ in range(n)] # 보드입력 받기
    ans = f(n)
    print(f"#{test_case} {ans}")