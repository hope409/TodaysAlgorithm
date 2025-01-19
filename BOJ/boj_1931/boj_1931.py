import heapq

n = int(input())

li = list()

for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(li, [start, end])

_, past = heapq.heappop(li)
cnt = 1
while li:
    start, end = heapq.heappop(li)

    if start >= past:
        cnt += 1
        past = end
        continue

print(cnt)