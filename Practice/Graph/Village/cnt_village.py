import sys
sys.stdin = open('s_input.txt')

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)
    if root_x == root_y:
        return
    parent[root_x] = root_y

def cnt_group():
    group_li = dict()
    for j in range(1, n + 1):
        root = find_parent(j)
        if root not in group_li:
            group_li[root] = []
        group_li[root].append(j)
    return len(group_li)

t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    parent = list(range(n + 1))
    for _ in range(m):
        x, y = map(int, input().split())
        union(x, y)
    result = cnt_group()
    print(f"#{test_case} {result}")