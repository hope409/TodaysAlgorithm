import sys
sys.stdin = open('sample_input.txt')

def bst_insert(node, num): # 그냥 끝에 삽입 할때
    bin_tree[node] = num
    if node != 1:
        p_node = node // 2 # 부모 노드번호
        while p_node>= 1 and bin_tree[node] < bin_tree[p_node]: # 규칙에 맞을 때까지 바꾸기
            bin_tree[node], bin_tree[p_node] = bin_tree[p_node], bin_tree[node]
            node, p_node = p_node, p_node // 2



t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 노드의 개수
    bin_tree = [0] * (n + 1) # 이진트리 저장할 리스트
    num_li = list(map(int, input().split())) # 주어진 숫자 리스트
    node = 0 # 현재 들어가있는 노드의 수

    for num in num_li: # 하나씩 가져오기 시작
        node += 1
        bst_insert(node, num)

    sum_grand = 0 # 조상 노드의 합
    while node: # 모든 조상 노드 다 더하기
        node //= 2 # 부모 노드 번호 구하기
        sum_grand += bin_tree[node]
    print(f"#{test_case} {sum_grand}")