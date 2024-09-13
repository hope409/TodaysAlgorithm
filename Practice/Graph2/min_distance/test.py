import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for test_case in range(1, t + 1):
    node, edge = map(int, input().split())
    adj_li = [{} for _ in range(node + 1)]
    for _ in range(edge):
        start, end, length = map(int, input().split())
        adj_li[start][end] = length
    for next in adj_li:
        for next2 in next:
            print(next2)