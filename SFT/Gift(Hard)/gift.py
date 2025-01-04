'''
7
0 1 -2 1 0 0 0
1 2
2 3
3 4
4 5
3 6
6 7
3
5 6 4
1 7 2
3 1 2
'''
from collections import defaultdict
n = int(input())
node_status = list(map(int, input().split()))
adj_li = defaultdict(list)
for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    adj_li[n1].append(n2)
    adj_li[n2].append(n1)

round_number = int(input())
for _ in range(round_number):
