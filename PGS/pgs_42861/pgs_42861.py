from collections import deque

def solution(n, costs):
    answer = 0
    adj_list = [[] for _ in range(n)]

    for s, e, cost in costs:
        adj_list[s].append([e, cost])
        adj_list[e].append([s, cost])
        answer += cost

    for start in range(n):
        queue = deque([[start, 0, [0] * n]])
        while queue:
            pre_node, pre_cost, visited = queue.popleft()
            visited = visited.copy()
            visited[pre_node] = 1
            if pre_cost > answer:
                continue
            if sum(visited) == n:
                if pre_cost < answer:
                    answer = pre_cost
                continue
            for next_node, cost in adj_list[pre_node]:
                if visited[next_node]:
                    continue
                queue.append([next_node, pre_cost + cost, visited])

    return answer

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))