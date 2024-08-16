import sys
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    str1 = input() # 문자열로 받아오기
    str2 = input()
    if str1 in str2: # 있는지 찾기
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")