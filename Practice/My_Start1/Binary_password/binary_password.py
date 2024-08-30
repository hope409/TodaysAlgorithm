import sys
sys.stdin = open('input.txt')

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
    n, m = map(int, input().split()) # 세로, 가로 길이
    pas_info = []
    for i in range(n): # 첫번째 줄부터 탐색
        li = list(map(int, input()))
        if pas_info: # 이미 패턴을 찾았다면?
            continue
        if sum(li): # 패턴이 있는 줄을 찾았을 때
            for j in range(m - 1, 0, -1): # 비밀번호 패턴 찾기 시작
                if li[j]: # 비밀번호 끝점을 찾았다면?
                    pas_info = li[j:j-56:-1] # 비밀번호 가져오기
                    break
    pas_info = pas_info[::-1]
    odd = 0
    eve = 0
    for k in range(8): # 비밀번호 찾기
        pre_num = find_password(pas_info[k*7:(k+1)*7])
        if k % 2: # 홀수번호라면?
            odd += pre_num
        else: # 짝수번호라면?
            eve += pre_num
    if (eve*3 + odd) % 10: # 10의 배수가 아니라면?
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} {eve + odd}")
