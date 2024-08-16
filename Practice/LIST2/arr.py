arr = [1, 2, 3, 4]

status_arr = list()
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                status_arr.append([arr[i] * bit[i] for i in range(4)])
print(status_arr)
print(len(status_arr))