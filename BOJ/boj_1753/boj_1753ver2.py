'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''
from collections import defaultdict
import heapq
v, e = map(int, input().split())
start = int(input())
adj_li = defaultdict(dict)
for _ in range(e):
    s, u, w = map(int, input().split())
    if adj_li[s][u] and w >= adj_li[s][u]:
        continue
    else:
        adj_li[s][u] = w

visited = [float('inf') for _ in range(v + 1)]
visited[start] = 0
queue = [(0, start)]
while queue:
    cur_cost, cur_node = heapq.heappop(queue)
    if cur_cost > visited[cur_node]:
        continue
    for next_node in adj_li[cur_node].keys():
        next_cost = cur_cost + adj_li[cur_node][next_node]
        if next_cost < visited[next_node]:
            visited[next_node] = next_cost
            heapq.heappush(queue, (next_cost, next_node))
for i in range(1, v + 1):
    if visited[i] == float('inf'):
        print('INF')
    else:
        print(visited[i])
