import sys
sys.stdin = open('sample_input.txt')

def binary_cal(node): # 계산
    if expression[node].isdigit(): # 숫자라면
        return int(expression[node])
    else: # 숫자가 아니라면?
        left_num = binary_cal(left_li[node])
        right_num = binary_cal(right_li[node])
        return left_num + right_num

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

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n, m, l = map(int, input().split()) # n : 노드의 개수 / m : 리프 노드의 개수 / l : 출력할 노드 번호
    expression = ['+'] * (n + 1) # 수식
    expression[0] = '0'
    left_li, right_li = make_binary(n)
    for _ in range(m):
        node, num = input().split()
        expression[int(node)] = num

    result = binary_cal(l) # 출력할 노드 번호를 루트로 입력
    print(f"#{test_case} {result}")