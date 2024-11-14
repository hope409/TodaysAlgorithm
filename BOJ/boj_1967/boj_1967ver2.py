from collections import defaultdict

n = int(input()) # 노드의 개수
node_li = set(range(1, n + 1))
adj_li = defaultdict(list) # 인접 가중치 리스트

for _ in range(n - 1):
    start, end, weight = map(int, input().split()) # 출발노드, 도착노드, 가중치
    adj_li[start].append([end, weight])
root_node = list(adj_li.keys())
root_node.sort(reverse=True)
print(adj_li)

weight_tree = dict()
for node in root_node:
    child_nodes = [child_node[0] for child_node in adj_li[node]]
    edge_weights = [child_node[1] for child_node in adj_li[node]]
    if all(weight_tree[child]
           for child in child_nodes):
        for child in child_nodes:
            if weight_tree[node]:
                weight_tree[node][0] = max(weight_tree[node][0], weight_tree[child][0])
                weight_tree[node][1] += weight_tree[child][0]
            else:
                weight_tree[node] = [weight_tree[child][0], weight_tree[child][0]]
    else:
        weight_tree[node] = [max(edge_weights), sum(edge_weights)]
        # if not weight_tree[node]:
        #
        #     weight_tree[node][0] = max(weight_tree[node][0], edge_weight)
        #     weight_tree[node][1] += edge_weight
        # else:
        #     weight_tree[node] = [edge_weight, edge_weight]
print(weight_tree[1])
