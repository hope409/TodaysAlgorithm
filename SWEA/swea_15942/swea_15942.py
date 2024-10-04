import sys
sys.stdin = open('2_input_sample.txt')

t = int(input())  # 테스트 케이스 개수 입력
for test_case in range(1, t + 1):  # 각 테스트 케이스에 대해 반복
    n, k = map(int, input().split())  # n: 행성의 개수, k: 초기 함선수
    planet_li = list(map(int, input().split()))  # 각 행성의 인구수를 리스트로 입력 받음
    planet_li.sort()  # 행성들의 인구수를 오름차순으로 정렬
    next_idx = 0  # 다음 행성을 가리키는 인덱스
    top = -1  # 스택의 상단 인덱스
    stack = [None] * n  # 스택을 n 크기로 초기화
    rem_pop = 0  # 스택에 있는 행성들의 인구수 합을 저장
    count = 0  # 동원한 횟수를 세기 위한 카운터

    # 스택이 비어있지 않거나, 아직 방문할 행성이 남아있는 동안 루프 실행
    while top > -1 or next_idx < n:
        # 다음 행성을 방문할 수 있을 때 (행성의 인구수가 현재 인구수 k 이하일 때)
        while next_idx < n and planet_li[next_idx] <= k:
            top += 1  # 스택의 상단을 하나 늘림
            stack[top] = planet_li[next_idx]  # 현재 행성의 인구수를 스택에 추가
            rem_pop += planet_li[next_idx]  # 스택에 추가된 행성 인구수를 총합에 더함
            next_idx += 1  # 다음 행성으로 이동

        # 모든 행성을 방문했고 스택에 있는 인구수 총합이 k 이하라면 루프 종료
        if next_idx == n and rem_pop <= k:
            top = -1  # 스택을 비움 (루프 탈출 조건)
            continue

        # 더 이상 방문할 수 있는 행성이 없고 스택도 비어 있으면, 정복 불가능
        if next_idx < n and top == -1:
            count = -1  # 정복 불가능한 경우 -1로 표시
            break

        # 스택에서 가장 상단에 있는 행성을 꺼내서 정복
        next_planet = stack[top]  # 스택의 가장 위에 있는 행성
        top -= 1  # 스택에서 하나 제거
        count += 1  # 동원한 횟수 증가
        k += next_planet  # 정복한 행성의 인구수를 현재 함선수에 더함
        rem_pop -= next_planet  # 스택에서 제거된 행성의 인구수를 총합에서 뺌

    # 결과 출력: 각 테스트 케이스의 번호와 동원한 횟수
    print(f"#{test_case} {count}")
