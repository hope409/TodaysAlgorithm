import sys
sys.stdin = open("C:\Users\SSAFY\Downloads\input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    num = int(input())
    ladder_li = list()
    row_li = list()
    # ladder_li에 사다리 배열 입력
    for i in range(100):
        ladder_li.append(list(map(int, input().split())))
    # 맨 아랫줄에서 2인 원소 위치 찾기
    for i in range(100):
        if ladder_li[0][i] == 1:
            row_li.append(i)

            break
    col = 0
    val = 99999999
    # 길찾기 시작
    for row in row_li:
        cnt = 0
        while col != 99:
            # 왼쪽에 1이 있다면? 왼쪽으로 이동
            if row != 0 and ladder_li[col][row-1] == 1:
                row = row - 1
                while ladder_li[col-1][row] == 0:
                    row = row - 1
                    cnt = cnt + 1
                col = col + 1
                cnt = cnt + 1
            # 오른쪽에 1이 있다면? 오른쪽으로 이동
            elif row != 99 and ladder_li[col][row+1] == 1:
                row = row + 1
                while ladder_li[col - 1][row] == 0:
                    row = row + 1
                    cnt = cnt + 1
                col = col + 1
                cnt = cnt + 1
            # 없다면? 위로 이동
            else:
                col = col + 1
                cnt = cnt + 1
        if cnt < val:
            val = cnt
            n = row

print(n)
    # print(f"#{num} {row_li[n]}")