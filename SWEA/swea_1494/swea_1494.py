import sys
sys.stdin = open('input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 지렁이의 수
    positions = [list(map(int, input().split())) for _ in range(n)]
    