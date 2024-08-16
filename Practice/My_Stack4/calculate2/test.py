exp = '3+4+5*6+7'


def prec(item):
    if item == '+':
        return 2
    elif item == '*':
        return 3


stack = []
postfix = ''

for e in exp:

    if e.isnumeric():
        print(f'숫자임 {e}')
        postfix += e

    else:
        print(f'기호임 {e}')
        while stack and prec(e) <= prec(stack[-1]):
            postfix += stack.pop()
        stack.append(e)
while stack:
    postfix += stack.pop()

    print('후위표현식: ', postfix)
    print('연산자 스택: ', stack)
    print()

# 계산 부분
stack2 = []
for idx2 in range(len(postfix)):  # 후위 표현식을 이용해서 계산 시작
    if postfix[idx2].isdigit():  # 숫자 일 때?
        stack2.append(postfix[idx2])
    else:  # 연산자 일때
        num1 = int(stack2.pop())  # 뒤에숫자
        num2 = int(stack2.pop())  # 앞에숫자
        if postfix[idx2] == '+':
            stack2.append(num1 + num2)  # 계산후 다시 넣기
        else:
            stack2.append(num1 * num2)
print(stack2[0])