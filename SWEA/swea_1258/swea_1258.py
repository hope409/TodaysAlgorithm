import sys
sys.stdin = open('input.txt', 'r')

def find_arr(col, row):
    i, j = 0, 0
    global arr
    while arr[col + i][row + j] != 0:
        

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split())))

