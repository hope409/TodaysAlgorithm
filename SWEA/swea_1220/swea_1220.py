# 입력은 1개행씩이 아니라 열단위로 알려준다.
try:
    # 파일을 읽는 코드
    T = 10
    for test_case in range(1, T + 10):
        cnt = 0
        N = int(input())
        arr = list()
        # 1번째 열 ~ 100번째 열 입력(세로)
        for _ in range(N):
            arr.append(list(map(int, input().split())))
        # 세로로 비교할 것이기 때문에 row먼저 반복문
        for row in range(N):
            val = 0
            for col in range(N):
                if arr[col][row] == 1:
                    val = 1
                elif arr[col][row] == 2 and val == 1:
                    val = 2
                    cnt = cnt + 1
        print(f"#{test_case} {cnt}")
except EOFError:
    # 입력 txt 문제로 EOF에러가 나는 것 같아서 예외처리
    pass