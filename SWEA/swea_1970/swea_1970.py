'''

# SWEA 1206번

# 문제 해석
> 1. 화폐의 총 갯수를 최소로 하려고 한다.
> 2. 높은 단위의 화폐를 최대한 많이 가져가야 한다.

# 발상
> 1. 화폐의 종류를 리스트로 입력해두고 반복문을 돌린다.
> 2. n자리 자연수의 각 자릿수를 구하는 방법과 같은 방법으로 화폐의 수를 구한다.

'''

T = int(input())
li = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for test_case in range(1, T + 1):
    money = int(input())
    unit_li = list()
    unit_li.append(f"#{test_case}")
    for unit in li:
        if money != 0:
            unit_li.append(money // unit)
            money = money % unit
        else:
            unit_li.append(0)

    print(*unit_li)
