from pprint import pprint

# 정점의 개수, 간선의 개수
V, E = map(int, input().split())

# 간선 정보
data = list(map(int, input().split()))

# 인접행렬 생성0
# 빈 도화지 만들기
matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    n1 = data[i*2]
    n2 = data[i*2 + 1]
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1

def DFS(start):
    stack = [start]
    visited = [0] * (V + 1)

    while stack:
        current = stack.pop()

        if visited[current] == 0:
            visited[current] = 1
            print(current, end=' ')

            for next in range(V, 0, -1):
                # 다음 노드들 중에
                # 1. 현재 노드와 간선으로 연결되어 있는지
                # 2. 방문한 적이 없는지
                if matrix[current][next] == 1 and visited[next] == 0:
                    stack.append(next)

