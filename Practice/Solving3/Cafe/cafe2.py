import sys
sys.stdin = open('sample_input.txt')

direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # 대각선 방향: 우하, 좌하, 좌상, 우상

def find_route(n, x, y, start_x, start_y, idx, cnt, turn_count):
    global max_cnt
    for i in range(2):  # 두 방향으로만 회전 가능 (지금 방향, 시계 반대 방향)
        ndir = (idx + i) % 4
        dx, dy = direction[ndir]
        nx, ny = x + dx, y + dy
        # 다음 위치가 격자 범위 내에 있는지 확인
        if 0 <= nx < n and 0 <= ny < n:
            # 시작점으로 돌아왔고, 경로 길이가 4 이상이며, 정확히 4번의 방향 전환이 이루어졌으면 경로 완성
            if nx == start_x and ny == start_y and cnt >= 4 and turn_count == 4:
                max_cnt = max(max_cnt, cnt)
                return
            # 방문하지 않았고, 중복된 디저트가 아니라면
            if not visited[nx][ny] and not count_arr[cafe_arr[nx][ny]]:
                visited[nx][ny] = True
                count_arr[cafe_arr[nx][ny]] = True
                # 방향이 바뀌는 경우 turn_count 증가
                find_route(n, nx, ny, start_x, start_y, ndir, cnt + 1, turn_count + (ndir != idx))
                visited[nx][ny] = False
                count_arr[cafe_arr[nx][ny]] = False


t = int(input())  # 테스트케이스 개수
for test_case in range(1, t + 1):
    n = int(input())  # 카페의 크기
    cafe_arr = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = -1  # 초기값을 -1로 설정 (경로가 없을 경우를 대비)

    # 모든 좌표를 출발점으로 설정
    for i in range(n):
        for j in range(n):
            visited = [[False] * n for _ in range(n)]  # 방문 체크 배열
            count_arr = [False] * 101  # 디저트 종류 체크 배열 (1~100)
            visited[i][j] = True
            count_arr[cafe_arr[i][j]] = True
            # 초기 방향 전환 횟수는 0으로 시작
            find_route(n, i, j, i, j, 0, 1, 0)  # 경로 탐색 시작
            visited[i][j] = False
            count_arr[cafe_arr[i][j]] = False

    print(f"#{test_case} {max_cnt}")
