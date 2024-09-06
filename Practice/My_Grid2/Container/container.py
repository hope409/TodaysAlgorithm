import sys
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스
for test_case in range(1, t + 1):
    n, m = map(int, input().split()) # n : 컨테이너 수 / m : 트럭 수
    containers = list(map(int, input().split())) # 컨테이너
    trucks = list(map(int, input().split())) # 트럭
    containers.sort() # 정렬
    trucks.sort()
    result = 0
    while trucks and containers: # 남은 트럭과 컨테이너가 있다면
        truck = trucks.pop() # 가장 큰거부터 꺼내오기
        container = containers.pop()
        if truck >= container: # 이상이면 합산
            result += container
        else:
            trucks.append(truck) # 트럭에 못넣었으면 다시 재배치
    print(f"#{test_case} {result}")

