import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    val = 1
    arr = list()
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    for col in range(9):
        sum_row = 0
        for row in range(9):
            # 열 계산
            sum_row = sum_row + arr[col][row]
        if sum_row != 45:
            val = 0
            break
    if val != 0:
        for row in range(9):
            sum_col = 0
            for col in range(9):
                # 행 계산
                sum_col = sum_col + arr[col][row]
            if sum_col != 45:
                val = 0
                break

        if val != 0:
            for col in range(0, 7, 3):
                sum_box = 0
                for row in range(0, 7, 3):
                    sum_box = (arr[col][row] + arr[col][row + 1] + arr[col][row + 2] +
                               arr[col + 1][row] + arr[col + 1][row + 1] + arr[col + 1][row + 2] +
                               arr[col + 2][row] + arr[col + 2][row + 1] + arr[col + 2][row + 2])
                if sum_box != 45:
                    val = 0
                    break
    print(f"#{test_case} {val}")