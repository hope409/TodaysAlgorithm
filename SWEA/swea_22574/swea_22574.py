import sys
sys.stdin = open('1_sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n, p = map(int, input().split()) # 기회 / 폭탄이 있는 층
    floor = 0 # 현재층
    queue = [] # 이동을 선택을 한 회차
    for i in range(1, n + 1):
        # 최대한 높이 올라가야 하니까 일단 계속 올라가기
        floor += i
        # 이동회차 갱신
        queue.append(i)
        # 만약에 이동하고 나니 폭탄이 있는 층에 멈췄다면?
        while floor == p:
            # 이동한 회차들 중에 가장 작은 회차를 먼저 빼보기
            remove_floor = queue.pop(0)
            # 계산을 해본후 p와 같지 않아지면 현채 층 갱신하여 while 탈출
            if floor - remove_floor != p:
                floor -= remove_floor
    print(floor)