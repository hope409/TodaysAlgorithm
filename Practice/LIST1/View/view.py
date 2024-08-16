import sys
sys.stdin = open('sample_input.txt')

def find_min(arr):
    min_val = None
    for elem in arr:
        if min_val == None:
            min_val = elem
        elif min_val > elem:
            min_val = elem
    return min_val


T = 10
for test_case in range(1, T + 1):

    n = int(input())
    arr = list()
    sol = 0
    arr = list(map(int, input().split()))
    # print(arr)

    for i in range(n):
        if i < 2 or i > n-3:
            continue
            print(i)
        else:
            # print(arr[i])
            # print(arr[(i-1)])
            # print(arr[(i-2)])
            l1 = arr[i] - arr[i-1]
            r1 = arr[i] - arr[i+1]
            l2 = arr[i] - arr[i-2]
            r2 = arr[i] - arr[i+2]
            # print(l2, l1, r1, r2)

            if l1 > 0 and r1 > 0 and l2 > 0 and r2 > 0:
                arr2 = list()
                arr2.append(l1)
                arr2.append(r1)
                arr2.append(l2)
                arr2.append(r2)
                # print(f"min(arr2) : {min(arr2)}")
                sol = sol + find_min(arr2)
    print(f"#{test_case} {sol}")