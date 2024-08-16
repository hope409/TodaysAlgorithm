import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t + 1):
    str1 = input()
    str_len = len(str1)
    status = 1
    for i in range(str_len // 2):
        if str1[i] != str1[str_len - 1 - i]:
            print(f"#{test_case} 0")
            status = 0
            break
    if status == 1:
        print(f"#{test_case} 1")