'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

def dfs(start = 1):
    if not adj_li[start]:
        return
    for next in adj_li[start]:
        if visited[next]:
            continue
        visited[next] = 1
        dfs(next)

n = int(input())
n_edge = int(input())
adj_li = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
visited[1] = 1
for _ in range(n_edge):
    node1, node2 = map(int, input().split())
    adj_li[node1].append(node2)
    adj_li[node2].append(node1)

dfs()
print(visited.count(1) - 1)

