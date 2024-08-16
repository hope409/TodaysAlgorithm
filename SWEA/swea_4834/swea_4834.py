import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num_li = list()
    num_li.extend(map(int, input()))
    num_li.sort()
    idx = n - 1
    val = None
    num = None
    while idx != 0:
        if val == None:
            num = num_li[idx]
            val = num_li.count(num_li[idx])
        elif num_li.count(num_li[idx]) > val:
            val = num_li.count(num_li[idx])
            num = num_li[idx]
        idx = idx - num_li.count(num_li[idx])
    print(f"#{test_case} {num} {val}")