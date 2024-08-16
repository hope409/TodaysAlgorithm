import sys
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    str_li = list() # 5개 문자열 담을 리스트
    max_len = 0 # 가장 긴 문자열의 길이
    for _ in range(5): # 5개의 문자열과 가장 긴 문자열 길이 할당
        pre_li = list(map(str, input()))
        str_li.append(pre_li)
        pre_len = len(pre_li)
        if pre_len > max_len:
            max_len = pre_len

    print(f"#{test_case}", end=' ') # 출력
    for row in range(max_len):
        for col in range(5): # 인덱스가 없는 경우 건너가기
            if len(str_li[col]) <= row:
                continue
            else:
                print(str_li[col][row], end='')
    print()

