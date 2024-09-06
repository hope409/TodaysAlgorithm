import sys
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n, m, c = map(int, input().split()) # n : 벌통들의 크기 / m : 벌통의 개수 / c : 꿀의 최대양
    honeys = [list(map(int, input().split())) for _ in range(n)] # 벌통들
    workers = [[0] * m for _ in range(2)]
    for i in range(n):
        for j in range(n - m + 1):
            li = honeys[i][j:j + m]
            li.sort()
            pre_sum = 0
            while pre_sum <= c:
                honey = honeys.pop()
                pre_sum += honey
                workers