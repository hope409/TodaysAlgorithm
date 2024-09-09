t = int(input())
for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    squence_li = list(map(int, input().split()))
    cnt = 0
    pre = 0
    for i in range(n):
        used = [False] * n
        while i < n:
            if pre == k:
                cnt += 1

                continue

            used[i] = True
            pre += squence_li[i]
            i += 1