import sys
sys.stdin = open('GNS_test_input.txt')

def change_number(string): # 문자열을 숫자로 바꾸는 함수
    if string[0] == 'Z':
        return 0
    elif string[0] == 'O':
        return 1
    elif string[0] == 'E':
        return 8
    elif string[0] == 'N':
        return 9
    elif string[0] == 'T':
        if string[1] == 'W':
            return 2
        else:
            return 3
    elif string[0] == 'F':
        if string[1] == 'O':
            return 4
        else:
            return 5
    else:
        if string[1] == 'I':
            return 6
        else:
            return 7

t = int(input()) # 테스트 케이스 개수
for test_case in range(1, t + 1): # 시작
    t_number, num = map(int, input().strip('#').split()) # 해시 빼고 숫자로 2개 받아오기
    str_num_li = list(map(str, input().split())) # 문자열 리스트 받아오기
    
    # 숫자의 종류와 개수 넣을 리스트 생성
    li = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt_li = [0] * 10

    for i in range(num): # 함수 돌리면서 해당 숫자 인덱스에 카운트
        elem = change_number(str_num_li[i])
        cnt_li[elem] += 1

    print(f"#{test_case}")

    for j in range(10): # 출력
        number_str = li[j]
        for _ in range(cnt_li[j]):
            print(number_str, end = ' ')
    print()
