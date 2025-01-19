t = int(input())
for test_case in range(1, t + 1):
    string = input()
    k = int(input())
    li = list(map(int, input().split()))
    cnt = sum(li) % len(string)
    if cnt < 0:
        cnt += len(string)
    print(string[cnt:] + string[:cnt])