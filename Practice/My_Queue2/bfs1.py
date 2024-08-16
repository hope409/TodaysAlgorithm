'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, v): # s : 시작점 / v : 마지막 정점
    # 준비
    visited = [0] * (v + 1) # visited 생성
    q = [] # 큐 생성
    q.append(s) # 시작점 인큐
    visited[s] = -1 # 시작점 방문(이큐되었음)
    # 탐색
    while q: # 탐색할 정점이 남아있으면
        t = q.pop(0) # t <- 디큐
        print(t) # 처리
        for w in adj_li[t]: # t에 인접이고, 인큐
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1

v, e = map(int, input().split()) # v : 마지막 정점 번호 / e : 간선 수
arr = list(map(int, input().split()))
adj_li = [[] for _ in range(v + 1)]
for i in range(e):
    v1, v2 = arr[i*2], arr[i*2 + 1]
    adj_li[v1].append(v2)
    adj_li[v2].append(v1) # 방향이 없는 경우

bfs(1, v) # 출발점, 정점수