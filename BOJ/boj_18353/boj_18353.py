###


###

n = int(input()) # 병사의 수
soldier_list = list(map(int, input().split())) # 병사 리스트
stack = []
count = 0
for i in range(n):

    for soldier in soldier_list[i + 1]:
        soldier_sort = [soldier]
        if soldier
        while soldier_sort and soldier_sort[-1] < soldier:
            stack.append(soldier_sort.pop())
            count += 1
        soldier_sort.append(soldier)
print(stack)
print(count)