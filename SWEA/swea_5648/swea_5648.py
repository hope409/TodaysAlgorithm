import sys
sys.stdin = open('sample_input.txt')

vectors = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 원자의 수
    xy_axis = [[0] * 4001 for _ in range(4001)]
    
    for _ in range(n):
        x, y, vector, energy = map(int, input().split())
        xy_axis[2000 + 2 * y][2000 + 2 * x] = [vector, energy]

    time = 0
    while time < 4000:
        for i in range(4001):
            for j in range(4001):
                if xy_axis[j][i]:
                    dy, dx = vector[xy_axis[j][i][0]]
                    if 0 <= i + dx < 4001 and 0 <= j + dy < 4001:
                        if xy_axis[j + dy][i + dy]:
