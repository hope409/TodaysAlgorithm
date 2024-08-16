import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n, m = tuple(map(int, input().split()))
    num_li = list(map(int, input().split()))

    max_sum = None
    min_sum = None
    for i in range(n + 1 - m):
        pre = 0
        for j in range(m):
            pre = pre + num_li[i + j]
        if max_sum == None:
            min_sum = pre
            max_sum = pre

        if pre > max_sum:
            max_sum = pre
        elif pre < min_sum:
            min_sum = pre
    print(f"#{test_case} {max_sum - min_sum}")
