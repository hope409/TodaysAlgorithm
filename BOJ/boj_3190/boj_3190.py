'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''

### 다음 행동을 반환해줄 함수
# 주어진 방향 전환 리스트를 확인한다.
# 현재 시간이 방향 전환 리스트에 존재하면
# 해당하는 값을 넣어주고
# 아니면 직진하게 한다.
### 받은 값을 바탕으로 행동을 한다.

from collections import deque

directions = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 우, 하, 좌, 상

n = int(input()) # 보드의 크기
board = [[0] * n for _ in range(n)]
k = int(input()) # 사과의 개수
for _ in range(k): # 사과를 배치
    col, row = map(int, input().split())
    board[col - 1][row - 1] = 1
l = int(input()) # 방향 변환 횟수
trans_direction = [(int(x), y) for x, y in (input().split() for _ in range(l))] # 시간 부분을 int로 변환
queue = deque(trans_direction)

h_col, h_row = 0, 0 # 머리 위치
snake = deque([[h_col, h_row]]) # 초기 뱀 위치
direction = 0
count = -1
dy, dx = directions[direction]
board[h_col][h_row] = 'H'  # 뱀의 머리 초기 위치

while True:
    count += 1 # 시간 증가
    # 방향 전환 처리
    if queue and count == queue[0][0]:  # 방향 전환 시간이 되었을 때
        trans_time, next_direction = queue.popleft()
        if next_direction == 'D':
            direction = (direction + 1) % 4  # 오른쪽 회전
        elif next_direction == 'L':
            direction = (direction - 1) % 4  # 왼쪽 회전
        dy, dx = directions[direction]

    # 머리 이동
    h_col += dy
    h_row += dx

    # 벽에 부딪혔는지 체크
    if not (0 <= h_col < n and 0 <= h_row < n):
        break

    # 머리가 몸통에 부딪혔는지 체크
    if board[h_col][h_row] == 'H':
        break

    # 사과가 있는지 체크
    if board[h_col][h_row] == 1:  # 사과가 있으면
        snake.append([h_col, h_row])  # 사과를 먹고, 꼬리를 유지 (길이가 늘어남)
        board[h_col][h_row] = 'H'  # 새로운 머리 위치 설정
    else:  # 사과가 없으면
        snake.append([h_col, h_row])  # 머리 추가
        t_col, t_row = snake.popleft()  # 꼬리 제거
        board[t_col][t_row] = 0  # 꼬리가 있던 자리는 빈 공간으로

    board[h_col][h_row] = 'H'  # 머리 위치 업데이트

print(count + 1)