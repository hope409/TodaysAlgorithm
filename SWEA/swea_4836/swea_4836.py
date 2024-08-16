import sys
sys.stdin = open('sample_input.txt', 'r')

def fill_up(li):
    global arr
    cnt = 0
    col1, row1, col2, row2, color = li
    if color == 1:
        for col in range(col1, col2 + 1):
            for row in range(row1, row2 + 1):
                if arr[col][row] == 0:
                    arr[col][row] = 1
                elif arr[col][row] == 2:
                    arr[col][row] = 3
                    cnt = cnt + 1

    elif color == 2:
        for col in range(col1, col2 + 1):
            for row in range(row1, row2 + 1):
                if arr[col][row] == 1:
                    arr[col][row] = 3
                    cnt = cnt + 1
                elif arr[col][row] == 0:
                    arr[col][row] = 2
    return cnt
    

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]
    info_li = list()
    for _ in range(n):
        info_li.append(list(map(int, input().split())))

    cnt = 0
    for i in range(n):
        cnt = cnt + fill_up(info_li[i])

    print(f"#{test_case} {cnt}")