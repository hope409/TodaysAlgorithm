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

n = int(input()) # 공간의 크기
space = [[0] * n for _ in range(n)]
fish_list = [[] for _ in range(7)]
for i in range(n):
    pre_space = list(map(int, input().split()))
    for j, size in enumerate(pre_space):
        if size == 9:
            shark_position = n * i + j
            continue
        elif size == 0:
            continue
        fish_list[size].append(n * i + j)
    space[i] = pre_space
fish_num = len(sum(fish_list, []))
used = []
time_count = 0
fish_count = 0
count = 0
shark_size = 2
while fish_count != fish_num:
    if count == shark_size:
        shark_size += 1
        count = 0
    possible_fish_list = sum(fish_list[1:shark_size], [])
    possible_fish_list.sort()
    next_length = None
    for next_fish in possible_fish_list:
        if next_fish in used:
            continue
        pre_length = move(shark_position, next_fish, shark_size)
        if next_length is None or pre_length < next_length:
            next_length = pre_length
            min_fish = next_fish
    count += 1
    used.append(min_fish)
    fish_count += 1
    shark_position = min_fish
    time_count += 1

print(time_count)