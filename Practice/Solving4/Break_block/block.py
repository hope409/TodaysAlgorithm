import sys
sys.stdin = open('sample_input.txt')

def shooting(n):
    if n == 0:
        for
    pass

t = int(input())
for test_case in range(1, t + 1):
    n, w, h = map(int, input().split())
    block_arr = [list(map(int, input().split())) for _ in range(h)]
    result = shooting(n)
    print(f"#{test_case} {result}")