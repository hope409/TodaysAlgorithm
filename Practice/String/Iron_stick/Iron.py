# import sys
# sys.stdin = open('sample_input.txt')
#
# t = int(input())
# for test_case in range(1, t + 1):
#     stick = str(input())
#     new_stick = stick.replace('()', '-')
#     print(new_stick)
#
#     cnt = new_stick.count('(')
#     val = 0
#     for i in range(len(new_stick)):
#         pre = 1
#         idx = 1
#         laser_cnt = 0
#         if new_stick[i] == '(':
#             while pre != 0:
#                 if new_stick[i + idx] == '(':
#                     pre += 1
#                 elif new_stick[i + idx] == '-':
#                     laser_cnt += 1
#                 elif new_stick[i + idx] == ')':
#                     pre -= 1
#                 idx += 1
#             val += laser_cnt + 1
#
#     print(f"#{test_case} {val}")

import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for test_case in range(1, t + 1):
    stick = str(input())
    val = 0
    pre = 0
    idx = 0
    laser_cnt = 0
    for idx in range(len(stick)):
        if stick[idx] == '(':
            pre += 1
        elif stick[idx] == ')':
            if stick[idx - 1] == '(':
                val += pre - 1
                pre -= 1
            else:
                pre -= 1


    print(f"#{test_case} {val}")