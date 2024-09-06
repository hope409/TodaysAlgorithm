c, r = map(int, input().split()) # 가로, 세로
k = int(input()) # 관객 번호
vector = [[1, 0], [0, 1], [-1, 0], [0, -1]] #하우상좌
concert_hall = [[0] * c for _ in range(r)]
num, x, y, direction = 0, 0, -1, 0 # 현재번호, x, y, 방향
dy, dx = vector[0]
while num < k and c * r >= k:
    y += dy
    x += dx
    num += 1
    concert_hall[y][x] = num
    if 0 <= y + dy < r and 0 <= x + dx < c and not concert_hall[y + dy][x + dx]: # 범위 내 이고 빈자리일 때
        continue
    direction = (direction + 1) % 4 # 다음벡터로 순회
    dy, dx = vector[direction]
if num:
    print(x + 1, y + 1)
else:
    print(0)