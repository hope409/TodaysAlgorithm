'''
3
1 3
2 4
3 5
'''

import heapq
n = int(input()) # 수업의 개수
classes = [tuple(map(int, input().split())) for _ in range(n)] # 수업 시간표
classes.sort(key=lambda x:x[0]) # 수업 시작시간을 기준으로 정렬
cnt = 0 # 필요한 강의실의 개수 카운트할 변수
heap = [] # 강의실의 끝나는 시간을 채워 넣을 리스트 / 최소힙으로 삽입하여 최소값을 가져올거임
for start, end in classes:
    cnt += 1 # 매번 새로운 강의실 추가
    # 만약에 강의중인 수업이 있었고
    # 가장 빨리끝나는 강의가 지금 시작하는 강의보다 전에 끝났다면?
    if heap and start >= heap[0]:
        cnt -= 1 # 다시 강의장 카운트 뺀후
        heapq.heappop(heap) # 최소힙에서 제거
    heapq.heappush(heap, end) # 이번에 시작하는 강의를 최소힙에 추가
print(cnt)