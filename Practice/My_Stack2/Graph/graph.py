import sys
from pprint import pprint
sys.stdin = open('sample_input.txt')

def DFS(start, V, G):
    stack = [start]
    visited = [0] * (V + 1)
    while stack:
        current = stack.pop()
        if current == G:
            return 1

        if visited[current] == 0:
            visited[current] = 1
            # print(current, end=' ')

            for next in range(V, 0, -1):
                # 다음 노드들 중에
                # 1. 현재 노드와 간선으로 연결되어 있는지
                # 2. 방문한 적이 없는지
                if matrix[current][next] == 1 and visited[next] == 0:
                    stack.append(next)
    return 0

t = int(input())
for test_case in range(1, t + 1):
    V, E = map(int, input().split())
    matrix = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        i, j = map(int, input().split())
        matrix[i][j] = 1
    # pprint(matrix)
    S, G = map(int, input().split())
    print(f"#{test_case} {DFS(S, V, G)}")