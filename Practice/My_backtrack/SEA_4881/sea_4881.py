import sys
sys.stdin = open('sample_input.txt')

def find_min_sum(n, pre_sum = 0, x = 0):
    global min_sum
    if x == n: # 숫자를 n개만큼 다 더했다면
        if min_sum is None or pre_sum < min_sum: # 최소값이거나 초기값이 없다면
            min_sum = pre_sum
        return
    for i in range(n):
        # 이미 사용한 숫자거나 초기값이 있는데 이미 최소값보다 커졌다면
        if used[i] or min_sum is not None and pre_sum > min_sum:
            continue
        used[i] = True # 더한 숫자 체크
        find_min_sum(n, pre_sum + num_arr[x][i], x + 1) # 다음 숫자 더하기
        used[i] = False # 더한 숫자 체크 해제

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n = int(input()) # 숫자의 개수
    num_arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = None # 최소합
    used = [False] * n # 더한 숫자 추적
    find_min_sum(n) # 최소합을 구하는 함수
    print(f"#{test_case} {min_sum}")