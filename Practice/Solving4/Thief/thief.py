import sys
sys.stdin = open('sample_input.txt')

direction = [[-1, 0], [1, 0], [0, -1], [0, 1], [0, 0]] # 상하좌우중
structure_li = [0, [0, 1, 2, 3, 4], [0, 1, 4], [2, 3, 4], [0, 3, 4], [1, 3, 4], [1, 2, 4], [0, 2, 4]] # 터널 구조물 타입

# n, m : 세로 가로 길이 / l : 주어진 시간 / k : 사용한 시간 / i, j : 현재 위치
def hide_position(n, m, l, k, i, j, x, y):
    global cnt
    structure_num = tunnel_map[i][j]
    if tunnel_map[i][j]: # 터널이 있다면?
        if x + y:
            for structure in structure_li[structure_num]:
                di, dj = direction[structure]
                if x + di == 0 and y + dj == 0:
                    break
            else:
                return
    else: # 터널이 없다면?
        return

    if k == l: # 이동시간이 다 되었다면
        visited[i][j] = 1
        cnt += 1
        return

    for structure in structure_li[structure_num]:
        di, dj = direction[structure]
        if 0 <= i + di < n and 0 <= j + dj < m:
            hide_position(n, m, l, k + 1, i + di, j + dj, di, dj)


t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    # n, m : 지하터널의 세로 가로 / r, c : 맨홀뚜껑의 위치 / l : 탈출 후 소요시간
    n, m, r, c, l = map(int, input().split())
    tunnel_map = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    hide_position(n, m, l, 1, r, c, 0, 0)
    print(f"#{test_case} {cnt}")