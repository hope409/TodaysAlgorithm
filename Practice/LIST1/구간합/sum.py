import sys
sys.stdin = open('input.txt')

t = int(input())
for test_case in range(1, t + 1):
    n , m = map(int, input().split())
    num_li = list(map(int, input().split()))
    
    max_sum = None
    min_sum = None

    for idx in range(n - m + 1):
        pre_sum = 0
        for i in range(m):
            pre_sum = pre_sum + num_li[idx + i]

        if max_sum == None:
            max_sum = pre_sum
            min_sum = pre_sum

        elif pre_sum > max_sum:
            max_sum = pre_sum

        elif pre_sum < min_sum:
            min_sum = pre_sum
    
    print(f"#{test_case} {max_sum - min_sum}")