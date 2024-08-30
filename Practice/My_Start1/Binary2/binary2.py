import sys
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = input() # 주어진 숫자
    below_point = len(n) - 2
    n = int(float(n) * 10**below_point)
    result = '' # 변환후 결과
    zero_point = 10**below_point
    while n:
        if len(result) > 12:
            result = 'overflow'
            break
        n *= 2
        if n >= zero_point:
            result += '1'
            n -= zero_point
        else:
            result += '0'

    print(f"#{test_case} {result}")