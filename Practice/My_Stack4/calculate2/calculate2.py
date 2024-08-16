import sys
sys.stdin = open('input.txt')

t = 10
for test_case in range(1, t + 1):
    length = int(input())

    num_str = input()
    postfix = ''
    stack = [0] * length
    top = -1
    icp = {'+': 1, '*': 2}  # 연산자 우선순위
    for i in range(length):
        if '0' <= num_str[i] <= '9':  # 피연산자인 경우
            postfix += num_str[i]
        else:  # 연산자인 경우
            if top > -1 and icp[stack[top]] >= icp[num_str[i]]:  # stack[top] 우선순위가 같거나 높으면  pop
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = num_str[i]
    while top > -1:  # 남아있는 연산자를 수식뒤에 붙임
        postfix += stack[top]
        top -= 1
    print(postfix)
    # print(top)

    stack2 = []
    for idx2 in range(length):  # 후위 표현식을 이용해서 계산 시작
        if postfix[idx2].isdigit():  # 숫자 일 때?
            stack2.append(postfix[idx2])
        else:  # 연산자 일때
            num1 = int(stack2.pop())  # 뒤에숫자
            num2 = int(stack2.pop())  # 앞에숫자
            if postfix[idx2] == '+':
                stack2.append(num1 + num2)  # 계산후 다시 넣기
            else:
                stack2.append(num1 * num2)
    print(f"#{test_case} {stack2[0]}")