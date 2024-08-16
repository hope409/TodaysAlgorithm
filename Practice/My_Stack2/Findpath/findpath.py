import sys
from pprint import pprint
sys.stdin = open('input.txt')

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


t = 10
for test_case in range(1, t + 1):
    # 테케번호, 간선개수
    t_num, E = map(int, input().split())
    # 출발지, 도착지
    start, goal = 0, 99
    # 간선 정보
    data = list(map(int, input().split()))
    # 인접행렬 생성
    matrix = [[0] * 100 for _ in range(100)]

    for i in range(E):
        n1 = data[i*2]
        n2 = data[i*2 + 1]
        matrix[n1][n2] = 1

    print(f"#{t_num} {DFS(start, 99, goal)}")