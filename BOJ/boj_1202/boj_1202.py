from collections import deque

n, k = map(int, input().split())
jewel_li = [list(map(int, input().split())) for _ in range(n)]
bag_li = list(int(input()) for _ in range(k))

jewel_li.sort()
bag_li.sort(reverse=True)