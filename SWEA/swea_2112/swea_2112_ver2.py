import sys
sys.stdin = open('sample_input.txt')

def check2(film):
    film_T = list(zip(*film))
    film_T = [1 if len(max(''.join(row).split('0'))) >= k or len(max(''.join(row).split('1'))) >= k else 0 for row in film_T]
    if 0 not in film_T:
        return True
    else:
        return False

def injection(film, cnt):
    global min_count
    if min_count is not None and cnt >= min_count:
        return

    if check2(film):
        if min_count is None or cnt < min_count:
            min_count = cnt
        return

    for i in range(d):
        if used[i]:
            continue
        # i번째 위치에 약물 x 투입
        used[i] = True
        root = film[i]
        for x in range(2):
            film[i] = f'{x}' * w
            if check2(film):
                if min_count is None or cnt < min_count:
                    min_count = cnt + 1
                return
            injection(film[:], cnt + 1)
            film[i] = root
            used[i] = False


t = int(input())
for test_case in range(1, t + 1):
    d, w, k = map(int, input().split())
    film_li = [input().replace(' ', '') for _ in range(d)]
    used = [False] * d
    min_count = None
    if not check2(film_li):
        injection(film_li[:], 1)
    else:
        print(f"#{test_case} 0")
        continue

    print(f"#{test_case} {min_count}")