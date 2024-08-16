import sys
sys.stdin = open('input.txt')

def find_subset(arr):
    status_arr = list()
    bit = [0] * 10
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
                                            status_arr.append([arr[i] * bit[i] for i in range(10)])
    return status_arr

def sum_arr(arr):
    result = 0
    for elem in arr:
        result += elem
    return result

t = int(input())
for test_case in range(1, t + 1):
    arr = list(map(int, input().split()))
    subset_li = find_subset(arr)

    status = 0
    for sub in subset_li[1:]:
        if sum_arr(sub) == 0:
            status = 1
            break
    print(f"#{test_case} {status}")