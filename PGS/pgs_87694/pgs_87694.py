from copy import deepcopy
from collections import deque
from pprint import pprint


# 좌표평면을 만드는 함수
def init_axis(rectangles):
    # 좌표평면에서 그려질 직사각형들 중 가장 오른쪽 좌표와 위쪽 좌표
    right, up = 0, 0
    for rectangle in rectangles:
        x1, y1, x2, y2 = rectangle
        up = max(y2, up)
        right = max(x2, right)
    # 인덱스 경계값을 계산하기 편하게 가장 끝부분을 0으로 감싸기
    return [[0] * ((right + 1) * 2) for _ in range((up + 1) * 2)]

# 주어진 사각형들을 겹쳐서 좌표평면에 채우는 함수
def fill_rectangle(rectangles):
    axis = init_axis(rectangles)
    for rectangle in rectangles:
        x1, y1, x2, y2 = rectangle
        for i in range(x1 * 2, x2 * 2 + 1):
            for j in range(y1 * 2, y2 * 2 + 1):
                axis[j][i] = 1
    pprint(axis)
    print()
    return axis

# 테두리만 남기고 내부를 비우는 함수
def erase_square(rectangles):
    axis = fill_rectangle(rectangles)
    # 테두리를 남길 새로운 좌표평면
    is_boarder = deepcopy(axis)
    # 테두리인지 내부인지 구분하기 위한 반복문 시작
    for i in range(len(axis[0])):
        for j in range(len(axis)):
            # 만들어진 도형의 일부분에 도착했을 때
            if axis[j][i]:
                # 주변 8칸의 합을 계산할 임시변수
                temp = 0
                for k in range(j - 1, j + 2):
                    for l in range(i - 1, i + 2):
                        temp += axis[k][l]
                # 합이 9라면 도형의 내부이므로 테두리 부분이 아님
                if temp == 9:
                    is_boarder[j][i] = 0
    pprint(is_boarder)
    return is_boarder

# 메인함수
def solution(rectangle, characterX, characterY, itemX, itemY):
    # 캐릭터로 부터 아이템까지의 최단 거리 계산
    axis = erase_square(rectangle)
    # 방향벡터 설정
    delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    queue = deque() # 다음 탐색할 정보
    visited = set() # 방문기록

    queue.append((characterX * 2, characterY * 2, 0)) # 처음위치 초기화
    visited.add((characterX * 2, characterY * 2)) # 첫번째 위치 방문기록
    min_distance = None
    # bfs 탐색 시작
    while queue:
        # 현재 살펴볼 좌표와 이동한 거리
        x, y, distance = queue.popleft()

        # 캐릭터가 아이템에 도착했다면?
        if x == itemX * 2 and y == itemY * 2:
            # 초기값이 할당이 되어있지 않거나 최소값이라면? 갱신
            if min_distance is None or distance < min_distance:
                min_distance = distance
            continue

        # 현재 거리가 최소값을 넘어 섰다면? 더이상 할 필요가 없다
        if min_distance is not None and distance >= min_distance:
            continue

        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            # 다음 부분이 테두리 인데 탐색한 부분이 아니라면?
            if axis[ny][nx] and (nx, ny) not in visited:
                queue.append((nx, ny, distance + 1))
                visited.add((nx, ny))
    # 좌표평면을 4배로 스케일업 했기 때문에 거리는 절반으로 나눠야한다.
    return min_distance // 2

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))

#######################################################################################