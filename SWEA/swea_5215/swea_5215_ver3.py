import sys
sys.stdin = open('sample_input.txt')

# dp
def make(max_cal, items):
    # dp 배열: 칼로리 제한 내에서 얻을 수 있는 최대 만족도를 저장
    dp = [0] * (max_cal + 1)

    # 각 재료에 대해 처리
    for satis, cal in items:
        # dp 배열을 업데이트 (이유: 중복 선택 방지)
        for c in range(max_cal, cal - 1, -1):
            # dp[c]는 현재까지 칼로리 c에서 최대 만족도
            # dp[c - cal] + satis는 현재 재료를 추가했을 때의 만족도
            dp[c] = max(dp[c], dp[c - cal] + satis)

    # dp 배열 중 가장 큰 값이 최대 만족도 (모든 칼로리 제한을 고려한 최대 만족도)
    return max(dp)


# 테스트 케이스 수 입력
t = int(input())
for test_case in range(1, t + 1):
    # n: 재료 개수, l: 칼로리 제한
    n, l = map(int, input().split())

    # 각 재료의 만족도와 칼로리 정보를 리스트로 입력받음
    igd_li = [list(map(int, input().split())) for _ in range(n)]

    # 동적 계획법으로 최대 만족도 계산
    result = make(l, igd_li)

    # 결과 출력
    print(f"#{test_case} {result}")
