import sys
sys.stdin = open('sample_input.txt')

def find_sebset(arr):
    status_arr = list()
    bit = [0] * 12
    for i1 in range(2):
        bit[0] = i1
        for i2 in range(2):
            bit[1] = i2
            for i3 in range(2):
                bit[2] = i3
                for i4 in range(2):
                    bit[3] = i4
                    for i5 in range(2):
                        bit[4] = i5
                        for i6 in range(2):
                            bit[5] = i6
                            for i7 in range(2):
                                bit[6] = i7
                                for i8 in range(2):
                                    bit[7] = i8
                                    for i9 in range(2):
                                        bit[8] = i9
                                        for i10 in range(2):
                                            bit[9] = i10
                                            for i11 in range(2):
                                                bit[10] = i11
                                                for i12 in range(2):
                                                    bit[11] = i12
                                                    status_arr.append([arr[i] * bit[i] for i in range(12)])
    return status_arr

def find_zero(arr):
    cnt = 0
    for elem in arr:
        if elem == 0:
            cnt += 1
    return cnt

def sum_arr(arr):
    result = 0
    for elem in arr:
        result += elem
    return result

t = int(input())
for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    arr = [i for i in range(1, 13)]
    subset_li = find_sebset(arr)
    status = False
    result = 0
    for sub in subset_li:
        if find_zero(sub) == 12 - n and sum_arr(sub) == k:
            status = True
            result += 1

    if status == True:
        print(f"#{test_case} {result}")

    else:
        print(f"#{test_case} 0")


status_arr = list()
bit = [0] * 2
for i0 in range(2):                                    # i0 = 0                 i0 = 1
    bit[0] = i0
    for i12 in range(2):                               # [0, 0] , [0, 1]        [1, 0],  [1, 1]
        bit[1] = i1
        status_arr.append([arr[i] * bit[i] for i in range(12)])

bit[0] = 0
bit[1] = 0
status_arr.append([arr[i] * bit[i] for i in range(2)])
bit[0] = 0
bit[1] = 1
status_arr.append([arr[i] * bit[i] for i in range(2)])
bit[0] = 1
bit[1] = 0
status_arr.append([arr[i] * bit[i] for i in range(2)])
bit[0] = 1
bit[1] = 1
status_arr.append([arr[i] * bit[i] for i in range(2)])