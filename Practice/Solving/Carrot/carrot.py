import sys
sys.stdin = open('carrot_sample_in.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n = int(input()) # 당근 개수
    carrot_li = list(map(int, input().split())) # 당근 크기 목록
    max_cnt = 0
    pre_cnt = 1
    for idx in range(1, n): # 연속 증가 확인
        if carrot_li[idx] > carrot_li[idx - 1]:
            pre_cnt += 1
        else:
            pre_cnt = 1

        if pre_cnt > max_cnt:
            max_cnt = pre_cnt
    print(f"#{test_case} {max_cnt}")