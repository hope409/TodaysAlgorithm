import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num_li = list(map(int, input().split()))
    min_num = None
    max_num = None
    for num in num_li:
        if min_num == None and max_num == None:
            min_num = num
            max_num = num
        elif num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    print(f"#{test_case} {max_num - min_num}")