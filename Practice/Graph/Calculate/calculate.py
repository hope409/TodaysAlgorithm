import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())