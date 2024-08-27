import sys
sys.stdin = open('sample_input.txt')

# 중위 탐색
def inorder(node): # 시작 노드
    if node:
        inorder(left[node])
        binary_tree.append(node)
        inorder(right[node])

def make_binary(n): # n : 가장 큰 노드의 값
    left_li = [0] * (n + 1)
    right_li = [0] * (n + 1)
    for i in range(1, n + 1):
        if i*2 > n: # 왼쪽 자식 번호 저장
            break
        left_li[i] = i*2
        if i*2 + 1 > n: # 오른쪽 자식 번호 저장
            break
        right_li[i] = i*2 + 1
    return left_li, right_li

# t = int(input()) # 테스트케이스 개수
# for test_case in range(1, t + 1): # 시작
for n in range(1, 33):

    # n = int(input()) # 가장 큰 자연수
    binary_tree = []
    left, right = make_binary(n)
    inorder(1) # 중위탐색 순서 만들기
    li = [0] * (n + 1) # 탐색 순서를 따라서 이진트리 만들기
    t = 1
    for node in binary_tree:
        li[node] = t
        t += 1
    # print(left)
    # print(right)
    # print(binary_tree)
    print(f"#{n}", li[1], li[n//2])
    # print(f"1 : {li[1]}, {n} : {li[n//2]}")