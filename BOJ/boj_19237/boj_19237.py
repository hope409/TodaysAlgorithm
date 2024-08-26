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

shark_grid = [list(map(int, input().split())) for _ in range(n)] # 격자의 초기 상태
shark_vector = [0] + [map(int, input().split())] # 상어의 초기 방향
shark_pattern = [0] + [[0] + [list(map(int, input().split())) for _ in range(4)] for _ in range(4)] # 상어들의 방향 우선순위
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

def move_shark(n, m, k):
    for num_shark in range(1, m + 1): # 1번 상어 부터 끝까지
        i, j = shark_position[num_shark] # 상어 위치 가져오기
        shark_grid[i][j] += (m + 1) * k # 냄새 남기기