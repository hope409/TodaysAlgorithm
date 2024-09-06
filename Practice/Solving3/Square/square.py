t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    num_arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n * n + 1)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(n):
            for k in range(4):
                dy, dx = direction[k][0], direction[k][1]
                ny = i + dy
                nx = j + dx

                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                if num_arr[ny][nx] == num_arr[i][j] + 1:
                    visited[num_arr[i][j]] = 1
                    break
    cnt = max_cnt = start = 0

    for i in range(n * n - 1, -1, -1):
        if visited[i]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1
            cnt = 0
    print(f"#{test_case} {start} {max_cnt + 1}")