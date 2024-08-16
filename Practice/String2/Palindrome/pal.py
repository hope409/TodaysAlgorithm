import sys
sys.stdin = open('sample_input.txt')

def palindrome(n, m, arr): # n : 전체 문자열길이, m : 찾을 문자열길이
    for i in range(n):
        for j in range(n - m + 1):
            for k in range(m // 2):
                if arr[i][j + k] != arr[i][m + j - 1 - k]:
                    break
            else:
                return arr[i][j : j + m + 1]

def palindrome2(n, m, arr):
    for i in range(n):
        for j in range(n - m + 1):
            if arr[i][i : i + m] == arr[::-1]:
                return True
    return False

def transpose(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr

t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    str_arr = [list(map(str, input())) for _ in range(n)]
    result = palindrome(n, m, str_arr)
    if result != None:
        print(f"#{test_case} {''.join(result)}")
        continue
    transpose_arr = transpose(str_arr)
    result2 = palindrome(n, m, transpose_arr)
    print(f"#{test_case} {''.join(result2)}")



