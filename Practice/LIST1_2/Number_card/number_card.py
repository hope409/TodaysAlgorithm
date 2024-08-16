import sys
sys.stdin = open('input.txt')

def find_max(arr):
    max_val = None
    for elem in arr:
        if max_val == None:
            max_val = elem
        elif max_val < elem:
            max_val = elem
    return max_val

def find_max2(arr):
    max_val = None
    idx = None
    for i in range(len(arr)):
        if max_val == None:
            max_val = arr[i]
            idx = i
        elif max_val <= arr[i]:
            max_val = arr[i]
            idx = i
    return idx, max_val

def counting(arr):
    k = find_max(arr)
    counting_arr = [0] * (k + 1)
    for i in range(len(arr)):
        counting_arr[arr[i]] += 1

    return counting_arr

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num_arr = list(map(int, input()))

    counting_num_arr = counting(num_arr)

    idx, cnt = find_max2(counting_num_arr)

    print(f"#{test_case} {idx} {cnt}")
