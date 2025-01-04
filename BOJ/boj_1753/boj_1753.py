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
from collections import defaultdict, deque
v, e = map(int, input().split())
start = int(input())
adj_li = defaultdict(list)
for _ in range(e):
    s, u, w = map(int, input().split())
    adj_li[s].append([u, w])

visited = [float('inf') for _ in range(v + 1)]
queue = deque([[start, 0]])
while queue:
    cur_node, cur_cost = queue.popleft()
    if cur_cost < visited[cur_node]:
        visited[cur_node] = cur_cost
    for next_node, edge_cost in adj_li[cur_node]:
        if cur_cost + edge_cost < visited[next_node]:
            queue.append([next_node, cur_cost + edge_cost])
for i in range(1, v + 1):
    if visited[i] == float('inf'):
        print('INF')
    else:
        print(visited[i])
