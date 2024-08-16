def f(n):
    global cnt
    cnt += 1
    if n == 1:
        return
    else:
        f(n - 1)

# cnt = 0

def f2(i, n):
    if i == n:
        return
    else:
        print(arr[i])
        f(i + 1), n
        return
