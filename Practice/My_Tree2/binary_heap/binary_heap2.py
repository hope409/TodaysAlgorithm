import sys
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n = int(input()) # 노드의 개수
    bin_tree = [0] + list(map(int, input().split())) # 이진트리 저장
    for node in range(n, 0, -1): # 마지막 노드 부터 비교 시작
        p_node = node // 2
        while node >= 1 and bin_tree[node] < bin_tree[p_node]:
            bin_tree[node], bin_tree[p_node] = bin_tree[p_node], bin_tree[node]
            node, p_node = p_node, p_node // 2
    sum_grand = 0
    while n:
        n //= 2 # 부모 노드 번호 구하기
        sum_grand += bin_tree[n]
    print(f"#{test_case} {sum_grand}")