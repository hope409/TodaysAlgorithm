import sys
sys.stdin = open('sample_input.txt')

def make(cal, pre_cal = 0, pre_satis = 0):
    global result

    for idx in range(n):
        if used[idx]:
            continue
        if pre_cal + igd_li[idx][1] > cal:
            if result is None or pre_satis > result:
                result = pre_satis
            return
        used[idx] = True
        make(cal, pre_cal + igd_li[idx][1], pre_satis + igd_li[idx][0])
        used[idx] = False

t = int(input())
for test_case in range(1, t + 1):
    n, l = map(int, input().split())
    used = [False] * n
    igd_li = [0] * n
    for i in range(n):
        igd_li[i] = list(map(int, input().split()))
    result = None
    make(l)
    print(f"#{test_case} {result}")