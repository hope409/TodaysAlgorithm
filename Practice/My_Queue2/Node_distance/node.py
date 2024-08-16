import sys
sys.stdin = open('sample_input.txt')
# [[], [5], [6, 9], [9, 5], [7, 8], [7, 1, 3], [2], [4, 5, 8], [4, 7], [2, 3]]
# def find_goal(s, v, g, cnt = 0): # s : 출발노드 / v : 노드의 수 / g : 도착노드 / cnt : 지나온 간선개수
#     global visited, find
#     if s == g:
#         visited = [0] * (v + 1)
#         visited[find] = 1
#         cnt_li.append(cnt)
#     else:
#         for idx in range(v + 1):
#             if g in adj_li[idx]:
#                 if cnt == 0:
#                     find = idx
#                 if visited[idx] == 0:
#                     visited[idx] = 1
#                     find_goal(s, v, idx, cnt + 1)

def bfs(s, v, g):  # 시작정점 s, 마지막 정점 v, 도착노드 g
    visited = [0] * (v + 1) # visited 생성
    q = []  # 큐 생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:  # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)  # 디큐
        for w in adj_li[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)  # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1 # 지나온 노드 수 = 지나온 간선의 수 + 1
    if visited[g] == 0: # 연결이 안되어 있을 경우
        return 0
    return visited[g] - 1

t = int(input()) # 테스트 케이스 개수
for test_case in range(1, t + 1):
    v, e = map(int, input().split()) # v : 노드의 수 / e : 간선의 수
    adj_li = [[] for _ in range(v + 1)]
    for _ in range(e):
        n1, n2 = map(int, input().split()) # n1 : 간선의 출발노드 / n2 : 간선의 도착노드
        adj_li[n1].append(n2)
        adj_li[n2].append(n1)

    s, g = map(int, input().split()) # s : 출발노드 / g : 도착노드
    print(f"#{test_case} {bfs(s, v, g)}")
