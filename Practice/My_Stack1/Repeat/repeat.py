import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for test_case in range(1, t + 1):
    string = input()
    stack = []
    for idx in range(len(string)):
        if not stack:
            stack.append(string[idx])
        elif string[idx] == stack[-1]:
            stack.pop()
        else:
            stack.append(string[idx])
    print(f"#{test_case} {len(stack)}")