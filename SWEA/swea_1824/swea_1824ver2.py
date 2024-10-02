import sys
sys.stdin = open('input.txt')

# 명령서
def order(r, c, dr=0, dc=0, memo=0):
    if order_li[r][c] == '<':
        return [(0, -1, memo)]
    elif order_li[r][c] == '>':
        return [(0, 1, memo)]
    elif order_li[r][c] == '^':
        return [(-1, 0, memo)]
    elif order_li[r][c] == 'v':
        return [(1, 0, memo)]
    elif order_li[r][c] == '_':
        if memo == 0:
            return [(0, 1, memo)]
        else:
            return [(0, -1, memo)]
    elif order_li[r][c] == '|':
        if memo == 0:
            return [(1, 0, memo)]
        else:
            return [(-1, 0, memo)]
    elif order_li[r][c] == '?':
        return [(0, 1, memo), (0, -1, memo), (1, 0, memo), (-1, 0, memo)]
    elif order_li[r][c] == '.':
        return [(dr, dc, memo)]
    elif order_li[r][c].isdigit():
        return [(dr, dc, int(order_li[r][c]))]
    # 0과 15를 벗어나면 반대로 돌아와야 하기 때문에 아래와 같이 연산
    elif order_li[r][c] == '+':
        return [(dr, dc, (memo + 1) % 16)]
    elif order_li[r][c] == '-':
        return [(dr, dc, (memo - 1) % 16)]

# 프로그램 시작 (스택을 이용한 DFS)
def start(r=0, c=0, delta_r=0, delta_c=1, memo=0):
    # 입력받은 다음 행동 할당
    stack = [(r, c, delta_r, delta_c, memo)]
    # 시행 기록
    visited = set()
    # @ 찾기 시작
    while stack:
        # 현재좌표 / 방향벡터 / 현재 저장된 값 할당
        r, c, delta_r, delta_c, memo = stack.pop()
        # 종료 조건 1
        if order_li[r][c] == '@':
            return True

        # 현재 상태 저장
        state = (r, c, memo, delta_r, delta_c)
        # 같은 행동 시행 여부 확인
        if state in visited:
            continue
        # 시행 여부 기록
        visited.add(state)
        # 다음 행동을 명령서에 따라서 가져오기
        next_moves = order(r, c, delta_r, delta_c, memo)
        # 다음 행동이 여러개 일 수도 있기때문에 반복문으로 구현 (? 일때는 4방향을 다 탐색)
        for next_delta_r, next_delta_c, next_memo in next_moves:
            # 만약에 범위를 벗어나면 반대방향으로 돌아와야 하기 때문에 아래와 같이 연산
            next_r = (r + next_delta_r) % row
            next_c = (c + next_delta_c) % col
            # 다음 좌표와 행동을 저장
            stack.append((next_r, next_c, next_delta_r, next_delta_c, next_memo))
    # while문 안에서 종료조건 1을 만나지 못하면 @에 도달하지 못한 것
    # 종료 조건 2
    return False

# 테스트 케이스 입력
t = int(input())
for test_case in range(1, t + 1):
    # 행, 열의 개수
    row, col = map(int, input().split())
    # 명령서 리스트
    order_li = [input() for _ in range(row)]
    result = start()
    if result:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")
