'''
# SWEA 1959번

# 문제 해석
> 1. 길이가 짧은 숫자열을 움직여 가면서 마주보는 숫자끼리 곱한다.
> 2. 곱합 값의 합들 중에서 최대값을 구한다.


# 발상
> 1. 구구단 출력하는 방법을 응용한다.
> 2. 밖으로 넘어가면 안된다.
> 3. 긴 숫자열의 길이와 짧은 숫자열의 길이의 차보다 1개더 많은 횟수만큼 합을 구한다.


'''

T = int(input())
for test_case in range(1, T + 1):
    val = list()
    a, b = map(int, input().split())
    num_li = list(map(int, input().split()))
    num_li2 = list(map(int, input().split()))

    n = min(a, b)
    m = max(a, b)

    for i in range(m - n + 1):
        value = 0
        for j in range(n):
            if len(num_li) < len(num_li2):
                value = value + num_li[j] * num_li2[j + i]
            else:
                value = value + num_li2[j] * num_li[j + i]
        val.append(value)

    print(f"#{test_case} {max(val)}")