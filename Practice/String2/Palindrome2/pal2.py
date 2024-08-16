import sys
sys.stdin = open('input.txt')

def palindrome(n, m, arr): # n : 전체 문자열길이, m : 찾을 문자열길이
    for i in range(n):
        for j in range(n - m + 1):
            for k in range(m // 2):
                if arr[i][j + k] != arr[i][m + j - 1 - k]:
                    break
            else:
                return True
    return False

def transpose(arr):
    tp_arr = [[0] * len(arr) for _ in range(len(arr[0]))]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            tp_arr[j][i] = arr[i][j]
    return tp_arr

t = 10
for test_case in range(1, t + 1):
    tc = int(input().strip())
    str_arr = [list(map(str, input())) for _ in range(100)]
    tp_arr = transpose(str_arr)
    for length in range(100, -1, -1):
        hoz_status = palindrome(100, length, str_arr)
        ver_status = palindrome(100, length, tp_arr)

        if hoz_status or ver_status:
            print(f"#{tc} {length}")
            break

