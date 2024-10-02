import sys
sys.stdin = open('input.txt')
import random

# 명령서
def order(r, c, dr = 0, dc = 0, memo = 0):
    # <	이동 방향을 왼쪽으로 바꾼다.
    if order_li[r][c] == '<':
        return (0, -1, memo)
    # >	이동 방향을 오른쪽으로 바꾼다.
    elif order_li[r][c] == '>':
        return (0, 1, memo)
    # ^	이동 방향을 위쪽으로 바꾼다.
    elif order_li[r][c] == '^':
        return (-1, 0, memo)
    # v	이동 방향을 아래쪽으로 바꾼다.
    elif order_li[r][c] == 'v':
        return (1, 0, memo)
    # _	메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
    elif order_li[r][c] == '_':
        if memo == 0:
            return (0, 1, memo)
        else:
            return (0, -1, memo)
    # |	메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
    elif order_li[r][c] == '|':
        if memo == 0:
            return (1, 0, memo)
        else:
            return (-1, 0, memo)
    # ?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다. 방향이 바뀔 확률은 네 방향 동일하다.
    elif order_li[r][c] == '?':
        direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # (delta_r, delta_c)
        return (direction[0], direction[1], memo)
    # .	아무 것도 하지 않는다.
    elif order_li[r][c] == '.':
        return (dr, dc, memo)
    # 0~9	메모리에 문자가 나타내는 값을 저장한다.
    elif order_li[r][c].isdigit():
        return (dr, dc, int(order_li[r][c]))
    # +	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다.
    elif order_li[r][c] == '+':
        return (dr, dc, (memo + 1) % 16)
    # -	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다.
    elif order_li[r][c] == '-':
        return (dr, dc, (memo - 1) % 16)

# 프로그램 시작
def start(r = 0, c = 0, delta_r = 0, delta_c = 1, memo = 0, visited = None):
    if visited is None:
        visited = set()
    if order_li[r][c] == '@':
        return True
    state = (r, c, memo)
    if state in visited:
        return False
    visited.add(state)
    delta_r, delta_c, next_memo = order(r, c, delta_r, delta_c, memo)
    return start((r + delta_r) % row, (c + delta_c) % col, delta_r, delta_c, next_memo, visited)

t = int(input())
for test_case in range(1, t + 1):
    # 행, 열의 개수
    row, col = map(int, input().split())
    order_li = [input() for _ in range(row)]
    result = start()
    if result:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")