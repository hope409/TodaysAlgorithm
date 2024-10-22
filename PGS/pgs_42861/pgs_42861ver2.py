import heapq

def solution(n, costs):
    visited = [False] * n  # 섬 방문 여부
    # 비용 0으로 시작하는 임의의 섬 선택 (비용, 섬번호)
    # 시작섬은 아무곳이나 가능함
    heap = [[0, 0]]
    # 최소비용을 넣을 정답변수
    answer = 0
    # 사용한 다리수를 체크할 변수
    edges_used = 0
    # 빈 인접리스트 생성
    adj_list = [[] for _ in range(n)]
    # 인접리스트 갱신
    for s, e, cost in costs:
        adj_list[s].append([e, cost])
        adj_list[e].append([s, cost])
    # 최소비용 찾기 시작
    while heap:
        # 지금 확인할 섬과 해당 섬까지 오는데 드는 비용
        cost, node = heapq.heappop(heap)

        # 이미 방문한 섬은 무시
        if visited[node]:
            continue

        # 현재 섬을 방문, 비용 처리 사용한 다리 개수 갱신
        visited[node] = True
        answer += cost
        edges_used += 1

        # 모든 섬이 연결되면 종료
        if edges_used == n:
            break

        # 현재 섬에 연결된 다리들을 탐색
        for next_node, next_cost in adj_list[node]:
            # 이미 방문한 섬이면 무시
            if not visited[next_node]:
                heapq.heappush(heap, [next_cost, next_node])

    return answer

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

