import sys
sys.stdin = open('input.txt')

def mirror_reverse_string(s):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if len(s) == 1: # 재귀함수 탈출 하는 조건
        if s == 'b':
            return 'd'
        elif s == 'd':
            return 'b'
        elif s == 'p':
            return 'q'
        elif s == 'q':
            return 'p'
    else: # 마지막 글자 맨앞에 놓고 마지막 글자 제외하고 다시 집어넣기
        if s[-1] == 'b':
            pre_str = 'd'
        elif s[-1] == 'd':
            pre_str = 'b'
        elif s[-1] == 'p':
            pre_str = 'q'
        elif s[-1] == 'q':
            pre_str = 'p'
        result = pre_str + mirror_reverse_string(s[:-1])

    return result

t = int(input())
for test_case in range(1, t + 1):
    str1 = input()
    print(f"#{test_case} {mirror_reverse_string(str1)}")

