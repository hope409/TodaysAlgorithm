'''
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
'''
from pprint import pprint

vector_li = [0, [-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우(인덱스1~4)
n, m, k = map(int, input().split()) # n : 격자의 크기 / m : 상어의 수 / k : 냄새가 사라지는 시간

shark_li = [x for x in range(1, m + 1)] # 상어 번호 리스트
shark_grid = [list(map(int, input().split())) for _ in range(n)] # 격자의 초기 상태
shark_vector = [0] + list(map(int, input().split())) # 상어의 초기 방향
shark_pattern = [0] + [[0] + [list(map(int, input().split())) for _ in range(4)] for _ in range(4)] # 상어들의 방향 우선순위
print(shark_vector)
pprint(shark_pattern)
shark_position = [0] * (m + 1) # 상어의 현재 위치를 저장할 곳
cnt = 0 # 찾은 상어의 수
for i in range(n):
    for j in range(n):
        if shark_grid[i][j] != 0:
            shark_position[shark_grid[i][j]] = [i, j]
            cnt += 1
            if cnt == m:
                break
print(shark_position)

def move_shark(n, m, k): # n : 격자의 크기 / m : 상어의 수 / k : 냄새가 사라지는 시간
    for num_shark in shark_li: # 상어 리스트 가져오기
        i, j = shark_position[num_shark] # 상어 위치 가져오기
        shark_grid[i][j] += (m + 1) * k # 냄새 남기기
        for vector in shark_pattern[num_shark][shark_vector[num_shark]]: # 방향 우선순위에 따라서 가져오기
            dx, dy = vector_li[vector]
            nx = i + dx
            ny = j + dy
            if 0 <= nx < n and 0 <= ny < n and shark_grid[nx][ny] == 0:
                shark_position[num_shark] = [nx, ny]  # 현재자리 저장
                shark_grid[nx][ny] = num_shark  # 현재위치로 이동
                status = 1
                break
        if status:
            break
        else:
            for vector in shark_pattern[num_shark][shark_vector[num_shark]]:  # 방향 우선순위에 따라서 가져오기
                dx, dy = vector_li[vector]
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < n and shark_grid[nx][ny] % (m + 1) == num_shark:


