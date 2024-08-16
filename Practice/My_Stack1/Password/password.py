import sys
sys.stdin = open('input.txt')

t = 10
for test_case in range(1, t + 1):
    length, string = map(str, input().split())
    stack = []
    for idx in range(int(length)):
        if not stack:
            stack.append(string[idx])
        elif string[idx] == stack[-1]:
            stack.pop()
        else:
            stack.append(string[idx])
    print(f"#{test_case}", end=  ' ')
    for num in stack:
        print(num, end='')
    print()