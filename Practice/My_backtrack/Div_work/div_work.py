import sys
sys.stdin = open('input.txt')

'''
1
3
13 0 50
12 70 90
25 60 100
'''

def distrib_work(x, n, pre_percent = 100): # x : 현재 배분한 일의 수 / n : 일의 총 개수 / pre_percent : 현재 확률
    global max_percent # 최대 확률
    if x == n: # 일을 다 분배 했다면
        if pre_percent > max_percent:
            max_percent = pre_percent
        return

    for i in range(n):
        if used[i] or pre_percent * schedule_li[x][i] / 100 <= max_percent: # 이미 배분한 사람이거나, 확률이 더 작아 졌다면?
            continue
        used[i] = True
        distrib_work(x + 1, n, pre_percent * schedule_li[x][i] / 100)
        used[i] = False

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n = int(input()) # 직원의 수
    schedule_li = [list(map(int, input().split())) for _ in range(n)]
    max_percent = 0
    used = [False] * n
    distrib_work(0, n)
    print(f"#{test_case} {'{:.6f}'.format(max_percent)}") # 6번째 자리까지 출력