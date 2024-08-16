t = int(input())
for test_case in range(1, t + 1):
    string = input()
    stack = []
    pre = 0
    result = 1
    for idx in range(len(string)):
        if string[idx] == '(':
            stack.append(string[idx])
            pre += 1
        elif string[idx] == '{':
            stack.append(string[idx])
            pre += 1
        elif string[idx] == ')':
            if pre > 0:
                if stack[-1] == '(':
                    stack.pop()
                    pre -= 1
                elif stack[-1] == '{':
                    result = 0
            else:
                result = 0
                break
        elif string[idx] == '}':
            if pre > 0:
                if stack[-1] == '{':
                    stack.pop()
                    pre -= 1
                elif stack[-1] == '(':
                    result = 0
                    break
            else:
                result = 0
                break
    if len(stack):
        result = 0

    print(f'#{test_case} {result}')