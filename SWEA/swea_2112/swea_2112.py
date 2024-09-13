import sys
sys.stdin = open('sample_input.txt')
from itertools import combinations

def check2(film, k):
    film_T = list(zip(*film))
    film_T = [1 if len(max(''.join(row).split('0'))) >= k or len(max(''.join(row).split('1'))) >= k else 0 for row in film_T]
    if 0 not in film_T:
        return True
    else:
        return False

def check(film, d, w, k):
    # 필름에서 막 하나씩 가져오기
    result = 0
    for i in range(d - 1):
        up_cell, down_cell = film[i], film[i + 1]
        status = bin(~(int(up_cell, 2) ^ int(down_cell, 2)) & 0xFF)[2:]
        result += int('0' * (8 - len(status)) + status)
    for _ in range(w):
        pre = result % 10
        if pre < k:
            return False
        result //= 10

    return True

def injection(film, d, w, k, cnt):
    global min_count
    if min_count is not None and cnt >= min_count:
        return
    for i in range(d):
        if used[i]:
            continue
        # i번째 위치에 약물 x 투입
        used[i] = True
        root = film[i]
        for x in range(2):
            film[i] = f'{x}' * w
            status = check2(film, k)
            if status:
                if min_count is None or cnt < min_count:
                    min_count = cnt
                return
            injection(film[:], d, w, k, cnt + 1)
        film[i] = root
        used[i] = False


t = int(input())
for test_case in range(1, t + 1):
    d, w, k = map(int, input().split())
    film_li = [input().replace(' ', '') for _ in range(d)]
    used = [False] * d
    min_count = None
    if not check2(film_li, k):
        injection(film_li[:], d, w, k, 0)
    else:
        print(f"#{test_case} 0")
        continue

    print(f"#{test_case} {min_count}")