'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# left, right 를 쓰는 버전
# 단, 입력이 반드시 각 노드당 최대 2번 씩만 들어온다고 가정한 코드
# 전위 순회(나 -> 왼쪽 -> 오른쪽)
def preorder(node):
    if node == 0:
        return

    print(node, end=' ')
    preorder(left[node])
    preorder(right[node])

# 중위 순회(왼쪽 -> 나 -> 오른쪽)
def inorder(node):
    if node == 0:
        return
    inorder(left[node])
    print(node, end= ' ')
    inorder(right[node])

# 후위 순회(왼쪽 -> 오른쪽 -> 나)
def postorder(node):
    if node == 0:
        return
    postorder(left[node])
    postorder(right[node])
    print(node, end=' ')


n = int(input()) # 정점의 개수(정점: 1 ~ n 번)
arr = list(map(int, input().split()))
left = [0] * (n + 1) # 왼쪽 자식 번호를 저장할 리스트
# ex) left[3] = 2 -> 3번 부모의 왼쪽 자식은 2다.
right = [0] * (n + 1) # 오른쪽 자식 번호를 저장할 리스트

for i in range(0, len(arr), 2):
    parent, child = arr[i], arr[i + 1]

    # 왼쪽 자식이 없다면, 왼쪽에 삽입
    if left[parent] == 0:
        left[parent] = child
    # 왼족 자식은 있는데, 오른쪽 자식이 없다면 오른쪽에 삽입
    else:
        right[parent] = child
print(left)
print(right)

root = 1 # 시작점은 1이다.
preorder(root)