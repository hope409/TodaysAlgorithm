def move(i, y, x, dir, board, piece_info, piece_inboard):
    delta = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]} # 우 좌 상 하
    ny, nx = y + delta[dir][0], x + delta[dir][1] # 다음칸 좌표 계산
    if board[ny][nx] == 2: # 다음칸이 파란색이라면
        dir += (-1) ** (dir % 2 + 1) # 방향을 바꾸고
        ny, nx = y + delta[dir][0], x + delta[dir][1]  # 다음칸 좌표 계싼

        if board[ny][nx] == 2: # 또 파란색이라면
            # 제라리에 대기
            return y, x, dir

    stack_index = piece_inboard[y][x].index(i) # 보드의 해당 칸에서 i가 위치한 인덱스 찾기
    moving_pieces = piece_inboard[y][x][stack_index:] # 해당 인덱스 부터 뒤쪽은 전부 이동
    piece_inboard[y][x] = piece_inboard[y][x][:stack_index] # 해당 칸에 움직이지 않은 애들 남기기

    if not board[ny][nx]: # 흰색이라면
        piece_inboard[ny][nx].extend(moving_pieces) # 움직인 칸에 갱신

    elif board[ny][nx] == 1: # 빨간색이라면
        moving_pieces.reverse() # 순서 뒤집고
        piece_inboard[ny][nx].extend(moving_pieces) # 움직인 칸에 갱신

    for piece in moving_pieces: # 내가 가지고 있는 말 정보 갱신
        piece_info[piece] = [ny, nx, piece_info[piece][2]]

    return ny, nx, dir

def main():
    n, k = map(int, input().split())
    board = [[2] * (n + 2) if i == 0 or i == n + 1 else [2] + list(map(int, input().split())) + [2] for i in range(n + 2)]
    piece_info = {i + 1 : list(map(int, input().split())) for i in range(k)}
    piece_inboard = [[[] for _ in range(n + 2)] for _ in range(n + 2)]

    for i, (y, x, dir) in piece_info.items(): # 보드에 초기값 세팅
        piece_inboard[y][x].append(i)

    cnt = 0 # 몇 턴인지 계산
    while cnt <= 1000: # 1000턴 넘어가면 종료
        cnt += 1
        for i in range(1, k + 1):
            y, x, dir = piece_info[i] # 정보 가져오기
            ny, nx, new_dir = move(i, y, x, dir, board, piece_info, piece_inboard) # 지금 말의 다음 좌표 계산
            piece_info[i] = [ny, nx, new_dir] # 본인 갱신 -> 왜? -> 양쪽이 다 파란색 이었을 경우 방향만 바뀐상태로 유지 되어야 하기 떄문

            if len(piece_inboard[ny][nx]) >= 4: # 4개 이상 쌓이면 종료
                return cnt

    return -1 # 넘어가면 -1 반환

print(main())