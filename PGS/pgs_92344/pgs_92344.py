def solution(board, skill):
    for skill_info in skill:
        skill_type, r1, c1, r2, c2, degree = skill_info
        for col in range(r1, r2 + 1): # 이 부분이 오래걸리는 거 같다.
            for row in range(c1, c2 + 1):
                board[col][row] += degree * (-1) ** (skill_type % 2)
    answer = sum(1 for x in sum(board, []) if x > 0)
    return answer

# 시간이 너무 오래걸림
# 그러면 시작과 끝만 표기해서 할 수 있는 방법이 없을까?

def solution(board, skill):
    answer = 0 # 초기값 세팅
    n, m = len(board), len(board[0]) # 전체 보드 사이즈 계산
    difference = [[0] * (m + 1) for _ in range(n + 1)] # 변화량을 기록할 보드와 같은 사이즈의 2차원 리스트
    for skill_info in skill: # 스킬을 체크
        skill_type, r1, c1, r2, c2, degree = skill_info
        # 1이 공격 2가 회복 즉 홀수 일땐 뺄셈, 짝수 일땐 덧셈이 연산되도록 수식 계산
        degree = degree * (-1) ** (skill_type % 2)
        difference[r1][c1] += degree # 시작 지점 표시
        difference[r1][c2 + 1] -= degree # 가로 사이즈 종료 지점 표시
        difference[r2 + 1][c1] -= degree # 세로 사이즈 종료 지점 표시
        difference[r2 + 1][c2 + 1] += degree # 위의 연산을 하다보면 마지막 한 곳이 비게 되므로 그 부분 만 덧셈 한번 시행

    for i in range(n):
        for j in range(m):
            difference[i][j + 1] += difference[i][j] # 가로로 먼저 쭉 계산

    for j in range(m):
        for i in range(n):
            difference[i + 1][j] += difference[i][j] # 이어서 가로로 그려진걸 세로로 쭉 계산

    for i in range(n):
        for j in range(m):
            board[i][j] += difference[i][j] # 계산된 변화량을 보드에 갱신
            if board[i][j] > 0: # 그 후 파괴 되지 않은 건물을 파악 후 카운팅
                answer += 1
    return answer