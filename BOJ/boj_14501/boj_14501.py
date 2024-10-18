'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''


n = int(input()) # 일할 날짜
work_list = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    work_list[i] = list(map(int, input().split()))
max_total = 0
stack = [[1, 0]] # 현재 확인할 날짜, 총 금액
while stack:
    today, total = stack.pop()
    if today == n + 1:
        if total > max_total:
            max_total = total
        continue
    period, pay = work_list[today]
    if today + 1 <= n:
        stack.append([today + 1, total])
    if today + period <= n + 1:
        stack.append([today + period, total + pay])
    elif total > max_total:
        max_total = total

print(max_total)