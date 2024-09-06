import sys
sys.stdin = open('input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    num, cnt = map(int, input().split()) # 숫자, 교환 횟수
    num = list(map(int, str(num))) # 리스트로 받아오기
    idx = 0 # 비교할 가장 좌측 인덱스
    while idx < len(num) and cnt: # 교환 시작
        idx_max = len(num) - num[::-1].index(max(num[idx:])) - 1 # 가장 오른쪽에 있는 최대값
        if idx != idx_max: # 최대값이 아니면
            num[idx], num[idx_max] = num[idx_max], num[idx] # 자리 바꾸기
            num[-idx - 1:] = sorted(num[-idx - 1:], reverse=True) # 최대값이 여러개 였다면 우리가 원하는대로 자리가 바뀌지 않음
            cnt -= 1
        idx += 1

    if cnt % 2: # 아직 회수가 남았을 때
        number_li = [0] * 10
        for number in num: # 같은 숫자가 있는지 체크
            number_li[number] += 1
            if number_li[number] > 1: # 서로 자리 바꿔서 회수 소모
                break
        else: # 같은 숫자가 없었다면
            num[-1], num[-2] = num[-2], num[-1] # 가장 우측 인덱스 끼리 자리 바꾸기
    print(f"#{test_case}", end=' ')
    for elem in num:
        print(elem, end='')
    print()

