import sys
sys.stdin = open('sample_input.txt')

def next_number(number):
    f_n = number // 2
    b_n = number - f_n
    next_f = f_n // 2 + f_n % 2
    next_b = b_n // 2 + f_n % 2
    return next_f + next_b

def f(i, j):    # i~j번까지의 승자를 찾는 함수
    if i==j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현

def win(player1, player2, idx1, idx2):
    if player1 < player2:
        if player1 == 1:
            return player1, idx1
        else:
            return player2, idx2
    else:
        if player2 == 1:
            return player2, idx2
        else:
            return player1, idx1


t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    pre_arr = list(map(int, input().split()))
    next_arr = next_number(n)
    # while pre_arr:
    #     stack = []
    #     stack.append(pre_arr.pop())
    top = -1
    while pre_arr != 1:
        top += 1
        player1, idx1 = pre_arr.pop(0), top
        top += 1
        player2, idx2 = pre_arr.pop(0), top
        print(win(player1, player2, idx1, idx2))
        next_arr.append(win(player1, player2, idx1, idx2))
    print(next_arr)




