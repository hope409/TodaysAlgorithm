import sys
sys.stdin = open("input.txt", "r")

def rot_90(arr, n):
    new_arr = list()
    for row in range(n):
        new_li = list()
        for col in range(n - 1, -1, -1):
            new_li.append(arr[col][row])
        new_arr.append(new_li)
    return new_arr


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list()
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    first = rot_90(arr, n)
    second = rot_90(first, n)
    third = rot_90(second, n)

    print(f"#{test_case}")
    for idx in range(n):
        print(f"{''.join(list(map(str, first[idx])))} {''.join(list(map(str, second[idx])))} {''.join(list(map(str, third[idx])))}")