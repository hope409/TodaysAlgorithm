import sys
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n = int(input()) # 배열의 크기
    count = [0] * (n + 1)
    num_arr = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): # 숫자 배열 받아오기
        num_arr[i][1:] = list(map(int, input().split()))
    print(num_arr)
    # max_sum = 0
    # for i in range(1, n + 1):
    #     count[i] = 1
    #     pre_sum += num_arr
    #     for j in range(1, n + 1):
    #         if count[j] != 1:
    #             count[j] = 1:
