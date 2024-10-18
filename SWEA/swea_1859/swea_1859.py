# import sys
# sys.stdin = open('input.txt')

def purchase_plan(price_list):
    stack = price_list[-1]
    max_profit = 0
    for i in range(n - 2, -1, -1):
        stack = max(stack, price_list[i])
        max_profit += stack - price_list[i]

    return max_profit

def purchase_plan2(price_list):
    stack = price_list[-1]
    max_profit = 0
    for i in price_list[::-1]:
        stack = max(stack, i)
        max_profit += stack - i

    return max_profit

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 알고있는 날짜수
    days = list(map(int, input().split()))
    result = purchase_plan(days)
    print(f"#{test_case} {result}")