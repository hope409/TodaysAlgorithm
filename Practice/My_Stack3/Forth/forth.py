import sys
from pprint import pprint
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    exps = list(input().split()) # 수식 저장
    stack = [] # 계산값 넣을 곳

    for elm in exps:
        if elm.isdigit(): # 숫자 일때
            stack.append(int(elm))
        elif elm == '.': # . 일때
            if len(stack) != 1:
                result = 'error'
                break
            else:
                result = stack[0]
                break
        else: # 연산자 일때
            if len(stack) < 2: # 피연산자가 2개보다 적을때
                result = 'error'
                break
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if elm == '+':
                    stack.append(num1 + num2)
                elif elm == '*':
                    stack.append(num1 * num2)
                elif elm == '/':
                    if num1 == 0:
                        result = 'error'
                    else:
                        stack.append(num1 // num2)
                elif elm == '-':
                    stack.append(num1 - num2)

    print(f"#{test_case} {result}")



