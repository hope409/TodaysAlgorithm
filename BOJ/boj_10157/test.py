def updown(x, y, d):
    global K
    if d > 0:
        nx = d
        for i in range(y-d + 1): 0~ y-d 까지
            if K:
                ny = d + i
                K -= 1
            else:
                print(nx, ny, end=' ')
        else:
            side(x, y, d)
    else:
        nx = x+1 - d
        for i in range(y+d+1

                       ):
            if K:
                ny = y - i
                K -= 1

    # for i in range(y+1 - abs(d)):     # 반복범위 0~ y-d
    #     if d > 0 and K:             # 한바퀴의 첫번째
    #         ny = d + i              # 현재 y값은 d+i
    #     elif d < 0 and K:           # 한바퀴의 3번째(내려갈때)
    #         ny = y+d+1-i            # 현재 y값은 요렇게
    #     else:
    #         print(x, ny, end=' ')   # K가 0이면 현재 x, y 값
    #         return
    #     K -= 1                      # 사람수 1명씩 줄이기
    # else:
    #     if d > 0:                   # 한바퀴 올라가기 끝나면
    #         side(x, y, d)           # 오른쪽으로 가자~
    #     else:                       # 내려가기 끝나면
    #         side(x, y, -d)          # 왼쪽으로 가자


def side(x, y, d):
    global K
    ny =
    for i in range(x - abs(d)):     # 반복범위 0 ~ x-1
        if d > 0 and K:             # 한바퀴의 두번째(오른쪽)
            nx = d+1 + i            # 현재 x 좌표
        elif d < 0 and K:
            nx = x + d
        else:
            print(x, ny)
            return
        K -= 1
    else:
        if d > 0:
            side(x, y, -d)
        else:
            side(x, y, d+1)

C, R = map(int, input().split())
K = int(input())


