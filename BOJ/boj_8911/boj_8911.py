'''
3
FFLF
FFRRFF
FFFBBBRFFFBBB
'''

direction = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 상우하좌

# 명령서
def order_li(order, pre_dir):
    if order == 'F':
        return pre_dir, direction[pre_dir]

    elif order == 'B':
        return pre_dir, direction[(pre_dir + 2) % 4]

    elif order == 'L':
        return (pre_dir - 1) % 4, (0, 0)

    elif order == 'R':
        return (pre_dir + 1) % 4, (0, 0)


# 들어온 값에 따라 행동 시행
def move(order, pre_dir):
    global y, x, l_my, l_mx, r_my, r_mx, next_dir
    next_dir, (dy, dx) = order_li(order, pre_dir)
    y, x = y + dy, x + dx
    l_my, r_my, l_mx, r_mx = min(y, l_my), max(y, r_my), min(x, l_mx), max(x, r_mx)
    return next_dir


t = int(input()) # 테케의 개수
for _ in range(t):
    y, x, l_my, l_mx, r_my, r_mx = 0, 0, 0, 0, 0, 0  # 좌우 최대 값
    precept = input()  # 명령문
    next_dir = 0
    for order in precept:
        next_dir = move(order, next_dir)

    print((r_my - l_my) * (r_mx - l_mx))