T = 10
for test_case in range(1, T + 1):
    num = int(input())
    ladder_li = list()
    # ladder_li에 사다리 배열 입력
    for i in range(100):
        ladder_li.append(list(map(int, input().split())))
    # 맨 아랫줄에서 2인 원소 위치 찾기
    for i in range(100):
        if ladder_li[99][i] == 2:
            row = i
            break
    col = 99
    # 길찾기 시작
    while col != 0:
        # 왼쪽에 1이 있다면? 왼쪽으로 이동
        if row != 0 and ladder_li[col][row-1] == 1:
            row = row - 1
            while ladder_li[col-1][row] == 0:
                row = row - 1
            col = col - 1
        # 오른쪽에 1이 있다면? 오른쪽으로 이동
        elif row != 99 and ladder_li[col][row+1] == 1:
            row = row + 1
            while ladder_li[col - 1][row] == 0:
                row = row + 1
            col = col - 1
        # 없다면? 위로 이동
        else:
            col = col - 1

    print(f"#{num} {row}")