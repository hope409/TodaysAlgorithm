import sys
from pprint import pprint
sys.stdin = open('input1.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n, m = map(int, input().split()) # n : 줄의 수 / m : 한줄의 풍선 수
    flower_li = [list(map(int, input().split())) for _ in range(n)] # 풍선의 배열
    vector_li = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우
    max_sum = 0 # 꽃가루 최대 값
    for x in range(n): # 세로 탐색
        for y in range(m): # 가로 탐색
            pre_sum = flower_li[x][y] # 현재 위치 합
            for dx, dy in vector_li: # 벡터탐색
                for num in range(1, flower_li[x][y] + 1): # 현재 위치의 크기만큼 벡터탐색
                    if 0 <= x + dx * num < n and 0 <= y + dy * num < m: # 해당 위치 값 더하기
                        pre_sum += flower_li[x + dx * num][y + dy * num]
            if pre_sum > max_sum:
                max_sum = pre_sum

    print(f"#{test_case} {max_sum}")