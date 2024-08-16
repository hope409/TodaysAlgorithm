import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n, k = tuple(map(int, input().split()))
    points = list(map(int, input().split()))

    max_sum = 0
    points.sort(reverse = True)
    for i in range(k):
        max_sum = max_sum + points[0 + i]

    print(f"#{test_case} {max_sum}")