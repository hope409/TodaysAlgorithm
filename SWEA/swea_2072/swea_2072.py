T = int(input())

for test_case in range(1, T + 1):
    arr2 = list()
    arr = list(map(int, input().split()))
    for i in arr:
        if i % 2 == 1:
            arr2.append(i)
    print(f"#{test_case} {sum(arr2)}")