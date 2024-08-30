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
    pas_info2 = []
    result = 0
    for i in range(n):  # 첫번째 줄부터 탐색
        patterns = input().strip('0')
        new_password = ''
        if patterns:
            for elements in patterns:
                if elements != '0':
                    new_password += elements
                elif elements == '0' and new_password:
                    pas_info.append(new_password)
                    new_password = ''
            if new_password:
                pas_info.append(new_password)
    pas_info = list(set(pas_info))
    # print(pas_info)
    for pattern in pas_info:
        code = int(pattern, 16)
        code = bin(code)[2:].strip('0')

        if len(code) % 56:
            k = len(code) // 56 + 1 # 두께
            cnt = 56 * k - len(code)
            pas_info2.append('0' * cnt + code)
        password = []
        for j in range(0, len(pas_info2), k):
            password.append(int(pas_info2[j]))
        print(password)
        odd = 0
        eve = 0
        for m in range(8):  # 비밀번호 찾기
            pre_num = find_password(password[m * 7:(m + 1) * 7])
            if m == 7:  # 검증 번호라면?
                check = pre_num
                continue
            elif m % 2:  # 홀수번호라면?
                odd += pre_num
            else:  # 짝수번호라면?
                eve += pre_num
        if (eve * 3 + odd + check) % 10:  # 10의 배수가 아니라면?
            continue
        else:
            result += eve + odd + check
print(f"#{test_case} {result}")
