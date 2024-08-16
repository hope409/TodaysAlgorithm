import sys
sys.stdin = open('input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 문자열 길이
    num_arr = list(input().split('0')) # 0을 제외하고 리스트로 담기
    max_len = 0
    for item in num_arr: # 가장 긴거 찾기
        pre_len = len(item)
        if pre_len > max_len:
            max_len = pre_len
    print(f"#{test_case} {max_len}")