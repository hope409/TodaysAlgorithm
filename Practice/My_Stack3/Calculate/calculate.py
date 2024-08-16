import sys
from pprint import pprint
sys.stdin = open('input.txt')

t = 10 # 테스트 케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 주어진 수식의 길이
    num_str = input() # 수식
    stack = [] # 임시 저장 공간
    back_write = [] # 후위표현식을 저장할 공간
    for idx in range(n): # 변환 시작
        if num_str[idx] == '+': # +연산자 일때?
            if stack: # 임시 저장공간이 비어있지 않으면
                back_write.append(stack.pop()) # 저장공간에 있는 걸 빼와서 저장
                stack.append(num_str[idx]) # 현재 값 임시 저장공간에 저장
            else:
                stack.append(num_str[idx]) # 비어있으면 저장
        else:
            back_write.append(int(num_str[idx])) # 숫자일 때?
    if stack:
        back_write.append(stack.pop()) # 맨 마지막 값 저장

    # print(*back_write)
    stack2 = []
    for idx2 in range(n): # 후위 표현식을 이용해서 계산 시작
        if back_write[idx2] != '+': # 숫자 일 때?
            stack2.append(back_write[idx2])
        else: # +연산자 일때
            num1 = stack2.pop() # 뒤에숫자 
            num2 = stack2.pop() # 앞에숫자
            stack2.append(num1 + num2) # 계산후 다시 넣기
    print(f"#{test_case} {stack2[0]}")
