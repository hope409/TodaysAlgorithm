import sys
sys.stdin = open('2_input_sample.txt')

t = int(input())  # 테스트 케이스 수 입력
for test_case in range(t):
    n, k = map(int, input().split())  # n: 행성 개수, k: 초기 함선 수
    planet_li = list(map(int, input().split()))  # 각 행성의 인구수 리스트
    planet_li.sort()  # 행성 인구수 리스트를 오름차순으로 정렬

    count = 0  # 병력 충원 횟수
    invadable = []  # 충원에 사용할 수 있는 행성 목록 (작은 행성)

    # 큰 행성부터 탐색하여 정복을 시도
    for planet in planet_li:
        while k < planet:
            # 병력이 부족한 경우, 작은 행성을 이용해 병력 충원
            if not invadable:
                count = -1  # 더 이상 충원할 방법이 없을 경우 불가능한 경우
                break

            # 가장 작은 행성을 이용해 병력을 충원 (pop으로 하나씩 소모)
            k += invadable.pop(0)  # 충원하면서 병력 증가
            count += 1  # 충원 횟수 증가

        if count == -1:
            break

        # 병력이 충분한 경우, 해당 행성을 정복하고 병력을 소모한 후 인구만큼 충원
        k += planet
        invadable.append(planet)  # 충원용으로 이 행성을 추가

    # 테스트 케이스 결과 출력
    print(count)
