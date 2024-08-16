import sys
sys.stdin = open('sample_input.txt')

def find_max(arr):
    max_val = None
    for elem in arr:
        if max_val == None:
            max_val = elem
        elif max_val < elem:
            max_val = elem
    return max_val

t = int(input())

for test_case in range(1, t + 1):
    str1 = list(set(input())) # 중복 제거하면서 받아오기
    str2 = list(input()) # 두번째 문자열
    # print(str1, str2)
    bit = [0] * len(str1) # 개수 카운트할 리스트
    for i in range(len(str1)): # 비교할 대상 첫번째 문자열에서 받기
        for alph in str2: # 비교하면서 카운트 시작
            if alph == str1[i]:
                bit[i] += 1
    print(f"#{test_case} {find_max(bit)}") # 최대값 출력