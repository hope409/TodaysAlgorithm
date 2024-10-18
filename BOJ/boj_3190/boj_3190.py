'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''

def move(head, tail):


n = int(input()) # 보드의 크기
board = [[0] * n for _ in range(n)]
k = int(input()) # 사과의 개수
for _ in range(k):
    col, row = map(int, input())
    board[col - 1][row - 1] = 1

l = int(input()) # 방향 변환 횟수
trans_direction = [tuple(input().split()) for _ in range(l)] # 방향전환 정보
head_position = [0, 0]
tail_position = [0, 0]
