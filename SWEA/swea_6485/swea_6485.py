import sys
sys.stdin = open('s_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    bus_stop = [0] * 5001 # 버스 정류장에 지나는 버스 노선의 수
    n = int(input()) # 버스 노선의 수
    for _ in range(n): # 노선 수 입력
        start, end = map(int, input().split())
        for idx in range(start, end + 1):
            bus_stop[idx] += 1
    p = int(input()) # 확인할 정류장의 수
    print(f"#{test_case}", end = ' ')
    for _ in range(p): # 출력
        num = int(input()) # 정류장 번호
        print(bus_stop[num], end= ' ')
    print()