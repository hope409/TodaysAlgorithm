import sys
sys.stdin = open('input.txt')

def sort_up(n, arr):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    sort_arr = sort_up(n, arr)
    print(f"#{test_case}", end=' ')
    print(*sort_arr)