# 해당 위치까지의 최대합을 저장하면서 가자 / 메모이제이션? DP?
# 주어진 삼각형 리스트와 같은 형태인 max_triangle을 정의
# 위층부터 계산하면서 내려간다.

def solution(triangle):
    height = len(triangle) # 높이 계산
    max_triangle = [[0] * x for x in range(1, height + 1)] # 주어진 삼각형의 모양과 같은 리스트 생성
    max_triangle[0][0] = triangle[0][0] # 초기값 설정
    for col in range(1, height): # 2층부터 계산시작
        for row in range(col + 1): # 가장 왼쪽부터 계산시작
            if row: # 맨왼쪽 값이 아닐때
                if row == col: # 맨 오른쪽 값 일때
                    # 해당자리는 왼쪽 위의 값에 현재 자리 값을 더한 값
                    max_triangle[col][row] = max_triangle[col - 1][row - 1] + triangle[col][row]
                else: # 중간에 있는 숫자 일때
                    # 해당자리는 왼쪽 위의 값과 바로 위의 값 중 큰 값에 현재 자리 값을 더한 값
                    max_triangle[col][row] = max(max_triangle[col - 1][row], max_triangle[col - 1][row - 1]) + triangle[col][row]
            else: # 맨 왼쪽 값 일때
                # 해당자리는 바로 위의 값과 현재 자리 값을 더한 값
                max_triangle[col][row] = max_triangle[col - 1][row] + triangle[col][row]
    # 맨 아래층이 계산이 완료 된 숫자들이고 그중 가장 큰걸 찾으면 된다.
    answer = max(max_triangle[height - 1])

    return answer