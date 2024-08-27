import sys
sys.stdin = open('input.txt')

def inorder(node):
    if node: # 자식노드가 존재 한다면?
        inorder(left_li[node])
        print(alpabet_li[node], end='')
        inorder(right_li[node])

t = 10 # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 정점의 개수
    left_li = [0] * (n + 1) # 왼쪽자식 번호 저장할 리스트
    right_li = [0] * (n + 1)  # 오른쪽 자식 번호 저장할 리스트
    alpabet_li = [0] * (n + 1) # 알파벳 저장할 리스트
    for _ in range(n): # 저장 시작
        # 나, 알파벳, 왼쪽 자식, 오른쪽 자식
        info = [0] * 4
        li = list(input().split())
        for i in range(len(li)):
            info[i] = li[i]
        p, alpa, left, right = info

        alpabet_li[int(p)] = alpa
        left_li[int(p)] = int(left)
        right_li[int(p)] = int(right)

    print(f"#{test_case}", end=' ')
    inorder(1)
    print()

