# n = int(input()) # 병사의 수
# soldier_list = list(map(int, input().split())) # 병사 리스트
# count_li = list(range(n, 0, -1))
# for i in range(n):
#     stack = [soldier_list[i]]
#     for number in range(i + 1, n):
#         while stack and stack[-1] < soldier_list[number]:
#             stack.pop()
#             count_li[i] -= 1
#         stack.append(soldier_list[number])
# print(count_li)
# print(n - max(count_li))
# ##################################################

n = int(input())  # 병사의 수
soldier_li = list(map(int, input().split()))  # 병사 리스트
count_li = [1] * n  # 각 병사마다의 최장 내림차순 길이를 기록할 리스트

for i in range(n - 2, -1, -1):  # 뒤에서부터 검사
    for j in range(i + 1, n):  # i 이후의 병사들과 비교
        if soldier_li[i] > soldier_li[j]:  # 내림차순 조건일 때
            count_li[i] = max(count_li[i], count_li[j] + 1)  # 내림차순 길이 갱신

print(n - max(count_li))  # 전체 병사 수에서 최장 내림차순 길이를 뺀 값 출력
