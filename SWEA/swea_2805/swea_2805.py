import sys

sys.stdin = open('input.txt', 'r')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 농장 크기
    farm_li = [list(map(int, input())) for _ in range(n)] # 농작물 수 배열
    # print(farm_li)
    val = 0 # 농작물의 총량
    for i in range(n // 2 + 1): # 행을 구분할 반복문
        for j in range(i + 1): # 열을 구분할 반복문
            if n // 2 + j != n // 2 - j: # 가운대 열부터 양옆으로 덧셈
                if i != n - 1 - i:
                    val += farm_li[i][n // 2 - j]
                    val += farm_li[i][n // 2 + j]
                    val += farm_li[n - 1 - i][n // 2 - j]
                    val += farm_li[n - 1 - i][n // 2 + j]
                else: # 가운대 일때는 한번만 덧셈
                    val += farm_li[i][n // 2 - j]
                    val += farm_li[i][n // 2 + j]
            else: # 가운대 행일때 한번만 덧셈
                if i != n - 1 - i:
                    val += farm_li[i][n // 2]
                    val += farm_li[n - 1 - i][n // 2]
                else:
                    val += farm_li[i][n // 2]

    print(f"#{test_case} {val}")