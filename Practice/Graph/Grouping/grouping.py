import sys
sys.stdin = open('sample_input.txt')

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

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n, m = map(int, input().split()) # 사람  수 / 신청서 수
    parent = list(range(n + 1))
    form_li = list(map(int, input().split()))
    for i in range(m):
        x, y = form_li[i * 2], form_li[i * 2 + 1]
        union(x, y)

    group_li = dict()
    for j in range(1, n + 1):
        root = find_parent(j)
        if root not in group_li:
            group_li[root] = []
        group_li[root].append(j)
    print(f"#{test_case} {len(group_li)}")