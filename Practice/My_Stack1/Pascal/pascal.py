import sys
sys.stdin = open('input.txt')

# t = int(input())
# for test_case in range(1, t + 1):
#     size = int(input())
#     pascal_arr = []
#     for i in range(1, size + 1):
#         stage = [1] * i
#         if i > 2:
#             for j in range(i):
#                 if j != 0 and j != i - 1:
#                     stage[j] = pascal_arr[i - 2][j - 1] + pascal_arr[i - 2][j]
#         pascal_arr.append(stage)
#     print(f"#{test_case}")
#     for floor in pascal_arr:
#         print(*floor)

def pascal():
    arr = []
    for i in range(1, 11):
        stage = [1] * i
        if i > 2:
            for j in range(i):
                if j != 0 and j != i - 1:
                    stage[j] = arr[i - 2][j - 1] + arr[i - 2][j]
        arr.append(stage)
    return arr

pascal_arr = pascal()
t = int(input())
for test_case in range(1, t + 1):
    size = int(input())
    print(f"#{test_case}")
    for i in range(size):
        print(*pascal_arr[i])