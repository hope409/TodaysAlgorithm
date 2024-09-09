import sys
sys.stdin = open('sample_input.txt')

# n : 수열의 개수 / k : 구하려는 합 / pre : 현재 합 / past : 방금 전 고른 인덱스
def find_sum(n, k, pre, past):
    global cnt
    # 현재 합이 구하려는 합과 같아 졌다면?
    if pre == k:
        cnt += 1
        return
    # 현재 합이 구하려는 합보다 커졌다면?
    if pre > k:
        return
    # 방금전 고른 인덱스 다음부터 시작
    for i in range(past + 1, n):
        find_sum(n, k, pre + squence_li[i], i)

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n, k = map(int, input().split()) # n : 수열의 개수 / k : 부분 수열의 합
    squence_li = list(map(int, input().split())) # 수열 리스트
    cnt = 0 # 개수 카운트
    find_sum(n, k, 0, -1) # 합이 k인 부분 수열 개수 찾기
    print(f"#{test_case} {cnt}")