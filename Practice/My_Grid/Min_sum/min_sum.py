import sys
sys.stdin = open('sample_input.txt')

vector = [[0, 1], [1, 0]] # 우 ㅅ
t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 판의 크기
    board = [list(map(int, input().split())) for _ in range(n)]
