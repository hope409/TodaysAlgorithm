import sys
sys.stdin = open('input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    # n : 사람 수 / m : 만드는 시간 / k : 한번에 만들 수 있는 붕어빵 수
    n, m, k = map(int, input().split())
    arrive = [0] * 11112 # 도착하는 시간대 카운트할 배열
    people_li = list(map(int, input().split())) # 도착 시간대 리스트
    for idx in people_li: # 사람이 도착하는 시간대 카운트
        arrive[idx] = 1

    sec = 0 # 초
    fish_bread = k * (-1) # 붕어빵 수
    result = 'Possible' # 결과
    while sec < 11112:
        if sec % m == 0: # 붕어빵이 만들어지는 때
            fish_bread += k

        if arrive[sec] == 1: # 사람이 도착 했을 때
            fish_bread -= 1
            n -= 1
            if fish_bread < 0: # 빵이 없었다면?
                result = 'Impossible'
                break
        if n == 0: # 모든사람이 왔다 갔다면?
            break
        sec += 1
    print(f"#{test_case} {result}")
