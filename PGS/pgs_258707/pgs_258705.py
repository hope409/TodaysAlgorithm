def solution(n, tops):
    # 총 타일 개수
    total_tiles = 2 * n + 1

    # DP 배열 초기화
    dp = [0] * (total_tiles + 1)
    dp[0] = 1  # 초기 조건
    dp[1] = 1  # 초기 조건

    # 점화식 계산
    for k in range(2, total_tiles + 1):
        if k % 2 == 0 and tops[k // 2 - 1]:
            dp[k] = (dp[k - 1] * 2 + dp[k - 2]) % 10007
        else:
            dp[k] = (dp[k - 1] + dp[k - 2]) % 10007

    answer = dp[total_tiles]

    return answer

# 테스트
n = 4
tops = [1, 1, 0, 1]
print(solution(n, tops) % 10007)  # n = 3인 경우 출력
