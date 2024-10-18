import heapq

n, m, k, x = map(int, input().split())
road = [[] for _ in range(n + 1)]
heap = []
for _ in range(m):
    start, end = map(int, input().split())
    road[start].append(end)

stack = [(x, set(), 0)] # 시작 위치 / 방문기록 / 이동 거리
while stack:
    start, visited, length = stack.pop()
    if length == k:
        heapq.heappush(heap, start)
        continue

    visited = visited.copy()
    visited.add(start)
    for next_node in road[start]:
        if next_node in visited:
            continue
        stack.append((next_node, visited, length + 1))
print(heap)

################################################################
import heapq

n, m, k, x = map(int, input().split())
road = [[] for _ in range(n + 1)]
heap = []
for _ in range(m):
    start, end = map(int, input().split())
    road[start].append(end)

# 최단거리 기록용 배열을 만들어 모든 거리를 무한대로 설정
shortest_distances = [float('inf')] * (n + 1)
shortest_distances[x] = 0  # 시작점은 거리 0

stack = [(x, 0)]  # 시작 위치 / 이동 거리
while stack:
    current_node, current_distance = stack.pop()

    # 만약 현재 이동 거리가 k라면, 힙에 추가
    if current_distance == k:
        heapq.heappush(heap, current_node)
        continue

    # 현재 노드에서 갈 수 있는 다음 노드 탐색
    for next_node in road[current_node]:
        # 이미 더 짧은 거리로 방문한 적이 있으면 패스
        if current_distance + 1 >= shortest_distances[next_node]:
            continue

        # 최단거리 갱신
        shortest_distances[next_node] = current_distance + 1
        stack.append((next_node, current_distance + 1))
if heap:
    while heap:
        print(heapq.heappop(heap))
else:
    print(-1)

###################################################################
import heapq
from collections import deque

n, m, k, x = map(int, input().split())
road = [[] for _ in range(n + 1)]
heap = []
for _ in range(m):
    start, end = map(int, input().split())
    road[start].append(end)

# 최단거리 기록용 배열을 만들어 모든 거리를 무한대로 설정
shortest_distances = [float('inf')] * (n + 1)
shortest_distances[x] = 0  # 시작점은 거리 0

queue = deque([(x, 0)])  # BFS 사용을 위한 큐
while queue:
    current_node, current_distance = queue.popleft()

    # 만약 현재 이동 거리가 k라면, 힙에 추가
    if current_distance == k:
        heapq.heappush(heap, current_node)
        continue

    # 현재 노드에서 갈 수 있는 다음 노드 탐색
    for next_node in road[current_node]:
        # 이미 더 짧은 거리로 방문한 적이 있으면 패스
        if current_distance + 1 >= shortest_distances[next_node]:
            continue

        # 최단거리 갱신
        shortest_distances[next_node] = current_distance + 1
        queue.append((next_node, current_distance + 1))

if heap:
    while heap:
        print(heapq.heappop(heap))
else:
    print(-1)
