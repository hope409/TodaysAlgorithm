arr = [['+'] * 5 for _ in range(5)]
for i in range(5):
    arr[i][i] = '#'
    for j in range(5):
        print(arr[i][j], end='')
    print()