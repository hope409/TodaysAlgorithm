'''
# SWEA 2001번

# 문제 해석
> 1. 자연수 2개를 입력받아 첫번째가 영역의 크기 두번째가 파리채의 크기이다.
> 2. 영역의 각 칸에는 파리의 수가 적혀있음
> 3. 파리채를 한번 휘둘렀을 때 가장 많은 파리를 잡은 경우를 찾는다.

# 발상
> 1. 파리채의 가장 왼쪽 위를 포인트로 잡고 영역 전체를 한번씩 훑는다.
> 2. 이때 파리채가 영역을 벗어나면 안된다.
> 3. 파리채의 포인트가 움직일 수 있는 범위는 파리채의 크기에 따라 다르다.
> 4. 영역이 5X5고 파리채가 2X2라면 파리채의 포인트는 (1,1)부터 (4,4)까지 움직일 수 있다.
> 5. 영역이 MXM고 파리채가 NXN라면 파리채의 포인트는 (1,1)부터 (M-N+1, M-N+1)까지 움직일 수 있다.

# 설계
> 1. 먼저 포인트를 1 ~ M-N+1 까지 반복시킨다.
> 2. 이 때 각 포인트에 위치했을 때 파리채의 1 ~ N 까지 반복해서 pre에 합산 시킨다.
> 3. pre가 max값보다 크다면 갱신시키며 1. 을 끝까지 반복한다.

'''

T = int(input())
for test_case in range(1, T + 1):
    m, n = map(int, input().split())
    max = 0
    pre = 0
    arr = list()
    
    for col in range(m):
        arr.append(list(map(int, input().split())))
    # print(arr)
    
    for i in range(m - n + 1):
        for j in range(m - n + 1):
            pre = 0
            for k in range(n):
                for l in range(n):
                    pre = pre + arr[i+k][j+l]
                    if pre >= max:
                        max = pre
                    # print(f"pre : {pre}")
                    # print(f"max : {max}")
    
    print(f"#{test_case} {max}")

