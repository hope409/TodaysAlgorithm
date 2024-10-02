direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
def move(start, end, shark_size):
    ey, ex = end // n, end % n
    min_length = None
    stack = [(start // n, start % n, 0)]
    while stack:
        y, x, length = stack.pop()
        if min_length is not None and length >= min_length:
            continue
        if ey == y and ex == x:
            if min_length is None or length < min_length:
                min_length = length
                continue
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if space[ny][nx] <= shark_size:
                    stack.append((ny, nx, length + 1))

    return min_length

def find(shark_size, shark_position):
    posible_fish_list = sum(fish_list[1:shark_size], [])



n = int(input()) # 공간의 크기
space = [[0] * n for _ in range(n)]
fish_list = [[] for _ in range(7)]
for i in range(n):
    pre_space = list(map(int, input().split()))
    for j, size in enumerate(pre_space):
        if size == 9:
            shark_position = n * i + j
            continue
        fish_list[size].append(n * i + j)
    space[i] = pre_space
print(fish_list)
print(space)