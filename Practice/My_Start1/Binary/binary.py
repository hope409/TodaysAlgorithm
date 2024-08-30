import sys
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n, hex_num = input().split() # n : 자리수 / hex : 16진수
    bin_num = '' # 이진수 담을 스트링
    for i in range(int(n)): # 자리수 만큼 체크
        pre_num = hex_num[i] # 현재 자리수
        if pre_num.isdigit(): # 숫자면?
            pre_num = int(pre_num)
        else: # 10이상인 숫자면?
            pre_num = ord(pre_num) - 55 # 아스키코드
        exp = 3 # 2**3 자리부터 확인 시작
        while exp != -1:
            digit = pre_num // 2 ** exp
            bin_num += str(digit)
            pre_num -= digit * 2**exp
            exp -= 1
    print(f"#{test_case} {bin_num}")