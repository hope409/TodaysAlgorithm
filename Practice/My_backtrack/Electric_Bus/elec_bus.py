import sys
sys.stdin = open('sample_input.txt')

def find_route(num, x = 0, cnt = -1):
    global min_change # 최소 교환 횟수
    if x >= num - 1: # 마지막 정류장에 도착 했을 때
        if min_change is None or cnt < min_change: # 초기값 이거나 최소값 이라면?
            min_change = cnt
        return
    if min_change is not None and cnt >= min_change: # 이미 최소보다 많이 교환 했다면?
        return
    remain = station_map[x] # 배터리 교환
    cnt += 1
    for move in range(1, remain + 1): # 잔여량 보다 적은 부분에서 이동
        find_route(num, x + move, cnt)


t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    num, *exchange_li = map(int, input().split())
    station_map = [0] * num
    for idx, battery in enumerate(exchange_li): # 정류장에 배터리 배치
        station_map[idx] = battery
    min_change = None
    find_route(num)

    print(f"#{test_case} {min_change}")

