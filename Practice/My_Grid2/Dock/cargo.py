import sys
sys.stdin = open('sample_input.txt')

def find_schedule(start = 0, cnt = 0): # start : 시작시간 / cnt : 이용한 화물차 수
    global max_cnt
    if start == 24:
        if cnt > max_cnt:
            max_cnt = cnt
        return
    if schedule[start]: # 현재 시각에 스케줄이 있다면
        for next_start in schedule[start]:
            find_schedule(next_start, cnt + 1)

    find_schedule(start + 1, cnt) # 현재 시각에 스케줄이 없거나 현재 스케줄을 무시할 때

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 신청서 개수
    schedule = [[] for _ in range(25)]
    max_cnt = 0
    for i in range(n):
        start, end = map(int, input().split()) # 시작시간, 종료시간
        schedule[start].append(end)
    find_schedule()
    print(f"#{test_case} {max_cnt}")