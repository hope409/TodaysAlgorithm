def solution(n, costs):
    answer = 0
    # 부모 노드를 찾는 함수
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    # 두 노드를 합치는 함수
    def union(parent, rank, x, y):
        rootX = find(parent, x)
        rootY = find(parent, y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    # 간선 비용을 기준으로 정렬
    costs.sort(key=lambda x: x[2])

    # 부모 노드와 rank 리스트 초기화
    parent = list(range(n))
    rank = [0] * n

    edges_used = 0

    # 모든 간선에 대해 처리
    for s, e, cost in costs:
        if find(parent, s) != find(parent, e):
            union(parent, rank, s, e)
            answer += cost
            edges_used += 1
            # 모든 정점이 연결된 경우 종료
            if edges_used == n - 1:
                break

    return answer