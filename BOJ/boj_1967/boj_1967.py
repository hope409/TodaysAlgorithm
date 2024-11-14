'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
'''
from collections import defaultdict

def dfs(start):
    max_cost = 0
    initial = adj_li[start][0]
    path_li = set()
    stack = [[initial, initial[1], {start}]] # 초기값 설정 : [[다음노드, 가중치], 비용, 방문기록]
    while stack:
        edge_info, cost, visited = stack.pop()
        # 다음 노드가 없다면?
        if edge_info[0] != start and edge_info[0] in leaf_node:
            # 최고 비용을 갱신
            if cost > max_cost:
                max_cost = cost
            continue
        visited = visited.copy()
        # 방문 처리
        visited.add(edge_info[0])
        # 다음 노드에 있는 모든 간선을 스택에 추가
        next_infos = adj_li[edge_info[0]]
        for next_info in next_infos:
            # 다음 노드에 방문한 적이 없고 start노드보다 더 작을때
            if next_info[0] not in visited and next_info[0] < start:
                stack.append([next_info, cost + next_info[1], visited])
    return max_cost

n = int(input()) # 노드의 개수
node_li = set(range(1, n + 1))
adj_li = defaultdict(list) # 인접 가중치 리스트

for _ in range(n - 1):
    start, end, weight = map(int, input().split()) # 출발노드, 도착노드, 가중치
    adj_li[start].append([end, weight])
    adj_li[end].append([start, weight])

# 리프노드 찾기
leaf_node = [node for node, value in adj_li.items() if len(value) == 1]
leaf_node.sort(reverse=True)
max_diameter = 0
for start in leaf_node:
    max_diameter = max(dfs(start), max_diameter)
print(max_diameter)