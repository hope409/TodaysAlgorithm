t = int(input())
for test_case in range(1, t + 1):
    men_li = list(map(int, input().split()))
    sum_tall = sum(men_li)
    remain = sum_tall % 7
    max_tall = max(men_li)
    result = (max_tall // 7 + 2) * 7 - remain
    print(result)