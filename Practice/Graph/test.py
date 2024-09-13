film = [input().replace(' ', '') for _ in range(6)]
# print(film)
result = 0
for i in range(5):
    up_cell, down_cell = film[i], film[i + 1]
    status = bin(int(up_cell, 2) ^ int(down_cell, 2))[2:]
    status2 = bin(~(int(up_cell, 2) ^ int(down_cell, 2)) & 0xFF)[2:]
    status = '0' * (8 - len(status)) + status
    status2 = int('0' * (8 - len(status2)) + status2)
    result += status2
    print(status)
    print(status2)
print(result)
x = 1
result = f'{x}' * 5
print(result)