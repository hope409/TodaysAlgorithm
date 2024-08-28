import sys
sys.stdin = open('input.txt')

def binary_cal(node):
    if expression[node].isdigit(): # 숫자라면
        return int(expression[node])
    else: # 숫자가 아니라면?
        left_num = binary_cal(left_li[node])
        right_num = binary_cal(right_li[node])
        # 연산 시작
        if expression[node] == '-':
            return left_num - right_num
        elif expression[node] == '+':
            return left_num + right_num
        elif expression[node] == '*':
            return left_num * right_num
        elif expression[node] == '/':
            return left_num // right_num

t = 10 # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 정점의 개수
    expression = [0] * (n + 1) # 수식
    left_li = [0] * (n + 1)
    right_li = [0] * (n + 1)
    for _ in range(n):
        node_info = [0] * 4
        input_li = list(input().split()) # 입력 값 리스트로 받기
        for i in range(len(input_li)):
            node_info[i] = input_li[i] # 노드정보에 넣기

        node, element, left, right = node_info

        expression[int(node)] = element
        left_li[int(node)] = int(left)
        right_li[int(node)] = int(right)

    result = binary_cal(1) # 해당 번호가 루트인 서브트리의 계산 결과
    print(f"#{test_case} {result}")

