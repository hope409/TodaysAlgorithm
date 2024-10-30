n = int(input()) # 배열의 개수
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

a_li.sort(reverse=True)
b_li.sort()

result = 0
for i in range(n):
    result += a_li[i] * b_li[i]
print(result)