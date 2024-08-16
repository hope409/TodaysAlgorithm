arr = [1, 2, 3]

# for i in range(1<<3):
#     # print(i)
#     for j in range(3):
#         if i & (1 << j):
#             print(f"{j}번 비트", end=' ')
#     print(f" = 숫자 {i}")
    #

# for i in range(1 << 3):
#     for j in range(3):
#         if i & (1 << j):
#             print(arr[j], end= ', ')
#     print()

# arr = list(range(1, 13))
# M = len(arr)  # 12
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())  # 3, 6
#     cnt = 0
#     for i in range(1 << M):  # 1*(2**12) : 0, 1, 2...,4095
#         ss = []  # 임시 부분집합 생성을 위한 리스트
#         for j in range(M):  # 12만큼 순회 : 0, 1, 2...,11
#             if i & (1 << j):  # i와 1*(2**j)
#                 ss.append(arr[j])
#         sum_ss = 0
#         for s in ss:
#             sum_ss += s
#
#         if len(ss) == N and sum_ss == K:
#             cnt += 1
#
#     print(f'#{tc} {cnt}')



subsets = [[]]
# 부분 집합 모두 구하기
for x in arr:
    for i in range(len(subsets)):
        subsets += [subsets[i] + [x]]
        print(i)
        print(subsets)

    # for s in subsets:
    #     s.sort()
    #
    # new_subsets = [[]]
    # for l in subsets:
    #     if l not in new_subsets:
    #         new_subsets += [l]
    # new_subsets
    #
    # count = 0
    # for k in new_subsets:
    #     total = 0
    #     for x in k:
    #         total += x
    #     if total == 0:
    #         count += 1
    # print(count)