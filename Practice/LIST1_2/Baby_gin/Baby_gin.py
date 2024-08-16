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

def counting(arr):
    k = find_max(arr)
    counting_arr = [0] * (k + 1)
    for i in range(len(arr)):
        counting_arr[arr[i]] += 1

    return counting_arr

def find_triplet(arr):
    for i in range(len(arr)):
        if arr[i] >= 3:
            arr[i] = arr[i] - 3
            return arr, True

    return arr, False

def find_run(arr):
    for i in range(len(arr) - 2):
        if arr[i] >= 1 and arr[i + 1] >= 1 and arr[i + 2] >= 1:
            arr[i] -= 1
            arr[i + 1] -= 1
            arr[i + 2] -= 1
            return arr, True
    return arr, False

T = int(input())

for test_case in range(1, T + 1):

    num_arr = list(map(int, input().strip()))

    counting_num_arr = counting(num_arr)
    counting_num_arr, status = find_triplet(counting_num_arr)

    if status == True:
        counting_num_arr, status = find_triplet(counting_num_arr)

        if status == True:
            print(f"#{test_case} 1")

        else:
            counting_num_arr, status = find_run(counting_num_arr)

            if status == True:
                print(f"#{test_case} 1")

            else:
                print(f"#{test_case} 0")

    else:
        counting_num_arr, status = find_run(counting_num_arr)

        if status == True:
            counting_num_arr, status = find_run(counting_num_arr)

            if status == True:
                print(f"#{test_case} 1")

            else:
                print(f"#{test_case} 0")

        else:
            print(f"#{test_case} 0")
