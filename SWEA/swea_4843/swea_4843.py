# li1 = [10, 9, 8, 7, 6]
# li2 = [1, 2, 3, 4, 5]
# li2.sort(reverse=True)

# num = 0
# li1_len = len(li1)
# for elem in li2:
#     if num == 0:
#         li1.append(elem)
#     else:
#         li1.insert(li1_len - num, elem)
#     num = num + 1
#     print(li1)

# print(li1)

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num_li = list(map(int, input().split()))
    num_li.sort(reverse = True)
    large_li = list()
    small_li = list()

    for idx in range(n):
        if idx < n / 2:
            large_li.append(num_li[idx])
        else:
            small_li.append(num_li[idx])
    # print(f"large_li : {large_li}")
    # print(f"small_li : {small_li}")

    num = 0
    small_li_len = len(small_li)
    for elem in small_li:
        if num == 0:
            large_li.append(elem)
        else:
            large_li.insert(small_li_len - num, elem)
        num = num + 1

    print(f"#{test_case} {' '.join(map(str, large_li[0:10]))}")