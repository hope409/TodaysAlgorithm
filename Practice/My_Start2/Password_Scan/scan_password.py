# import sys
# sys.stdin = open('sample_input.txt')

def find_password(pwd):
    if sum(pwd) == 3:
        if pwd[1]: # 해당 자리가 1이면
            if pwd[2]:
                return 5
            else:
                return 4
        elif pwd[2]: # 해당 자리가 1이면
            if pwd[3]:
                return 1
            else:
                return 2
        else:
            if pwd[5]:
                return 9
            else:
                return 0
    else: # 합이 5라면?
        if not pwd[2]: # 해당 자리가 0이면
            return 6
        elif not pwd[3]:
            return 8
        elif not pwd[4]:
            return 7
        else:
            return 3


t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n, m = map(int, input().split()) # n : 세로 길이 / m : 가로 길이
    pas_info = []
    patterns = []
    for i in range(n):  # 첫번째 줄부터 탐색
        pattern_li = list(input().strip('0').split('000000'))
        patterns.append(pattern_li)
        for pattern in pattern_li:
            if not pattern:
                continue
            code = int(pattern, 16)
            code = bin(code)[2:].strip('0')

            if len(code) % 56:
                k = len(code) // 56 + 1 # 두께
                cnt = 56 * k - len(code)
                pas_info.append('0' * cnt + code)
    pas_info = list(set(pas_info))
    result = 0
    for password in pas_info:
        odd = 0
        eve = 0
        password_li = []
        width = len(password) // 56 # 두께
        for j in range(0, len(password), width):
            password_li.append(int(password[j]))

        # print(password_li)
        for k in range(8):  # 비밀번호 찾기
            pre_num = find_password(password_li[k * 7:(k + 1) * 7])
            print(pre_num, end= '')
            if k == 7: # 검증 번호라면?
                check = pre_num
                continue
            elif k % 2:  # 홀수번호라면?
                odd += pre_num
            else:  # 짝수번호라면?
                eve += pre_num
        if (eve * 3 + odd + check) % 10:  # 10의 배수가 아니라면?
            continue
        else:
            result += eve + odd + check
    print(f"#{test_case} {result}")