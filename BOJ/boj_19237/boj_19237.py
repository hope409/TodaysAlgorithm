'''
4 5 6
0 0 0 0
0 3 0 0
2 0 1 0
0 4 0 5
3 4 2 1 3
4 1 3 2
4 2 3 1
1 2 4 3
2 3 1 4
1 3 2 4
4 1 3 2
4 3 2 1
1 4 3 2
2 3 1 4
4 3 2 1
1 4 3 2
4 2 3 1
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
2 3 1 4
3 2 4 1
2 3 4 1
1 2 4 3

'''
from pprint import pprint
def move_shark(n, m, k): # n : 격자의 크기 / m : 상어의 수 / k : 냄새가 사라지는 시간
    position = [1] * (m + 1)  # 빈자리로 갔는지 ?
    for num_shark in shark_li: # 상어 리스트 가져오기
        status = 0
        smell = (m + 1) * k # 현재 냄새
        i, j = shark_position[num_shark] # 상어 위치 가져오기
        for vector in shark_pattern[num_shark][shark_vector[num_shark]]: # 방향 우선순위에 따라서 가져오기
            dx, dy = vector_li[vector]
            nx = i + dx
            ny = j + dy
            if 0 <= nx < n and 0 <= ny < n: # 빈자리 먼저 찾아보기
                if shark_grid[nx][ny] == 0:
                    shark_position[num_shark] = [nx, ny]  # 현재자리 저장
                    shark_grid[nx][ny] = num_shark + smell # 현재위치로 이동
                    shark_vector[num_shark] = vector
                    status = 1
                    break
                elif smell < shark_grid[nx][ny] < num_shark + smell: # 누군가가 방금 남긴 냄새라면?
                    position_num_shark = shark_grid[nx][ny] % (m + 1) # 지금 자리의 주인
                    if not position[position_num_shark]: # 그자리가 빈자리가 아니였다면?
                        continue # 다음자리 확인
                    shark_li.remove(num_shark) # 해당 상어 격자에서 추방
                    status = 1
                    break

        if status: # 빈자리로 이동또는 추방 되었다면?
            continue
        for vector in shark_pattern[num_shark][shark_vector[num_shark]]:  # 방향 우선순위에 따라서 가져오기
            dx, dy = vector_li[vector]
            nx = i + dx
            ny = j + dy
            if 0 <= nx < n and 0 <= ny < n and shark_grid[nx][ny] % (m + 1) == num_shark: # 본인 냄새가 남겨져 있는 곳이면?
                shark_position[num_shark] = [nx, ny] # 현재자리 저장
                shark_grid[nx][ny] = num_shark + smell # 현재위치로 이동
                shark_vector[num_shark] = vector
                position[num_shark] = 0 # 빈자리로 갔는가? FALSE
                break
    for x in range(n):
        for y in range(n):
            shark_grid[x][y] -= m + 1
            if shark_grid[x][y] < 0:
                shark_grid[x][y] = 0

vector_li = [0, [-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우(인덱스1~4)
n, m, k = map(int, input().split()) # n : 격자의 크기 / m : 상어의 수 / k : 냄새가 사라지는 시간

shark_li = [x for x in range(1, m + 1)] # 상어 번호 리스트
shark_grid = [list(map(int, input().split())) for _ in range(n)] # 격자의 초기 상태
shark_vector = [0] + list(map(int, input().split())) # 상어의 초기 방향
shark_pattern = [0] + [[0] + [list(map(int, input().split())) for _ in range(4)] for _ in range(m)] # 상어들의 방향 우선순위
shark_position = [0] * (m + 1) # 상어의 현재 위치를 저장할 곳
cnt = 0 # 찾은 상어의 수
for i in range(n):
    for j in range(n):
        if shark_grid[i][j] != 0:
            shark_position[shark_grid[i][j]] = [i, j]
            shark_grid[i][j] += (m + 1) * (k - 1)  # 냄새 남기기
            cnt += 1
            if cnt == m:
                break

time = 0 # 시간 카운트
while time <= 1000 and len(shark_li) > 1: # 1000초 까지 혹은 상어가 한마리 남을 때 까지만
    time += 1
    move_shark(n, m, k) # 상어 움직이기

if len(shark_li) > 1:
    print(-1)
else:
    print(time)