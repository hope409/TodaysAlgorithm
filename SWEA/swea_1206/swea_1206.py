'''

# SWEA 1206번

# 문제 해석
> 1. 양옆의 맨끝 2칸은 비어있다.
> 2. 양옆에 2칸이 비어있는 공간일 때 조망권이 확보된다.
> 3. 기준건물이 양옆의 건물 2개보다 층수가 높아야 조망권 확보 가능하다고 볼 수 있다.

# 발상
> 1. 기준건물이 높아야 하니까 양옆의 건물높이를 기준건물높이에 뺄셈한다.
> 2. 음수가 나온다면 기준건물이 더 낮은 것 = 조망권 없음
> 3. 뺼셈한 4개의 수가 곧 기준 건물이 확보한 양옆의 빈칸 수
> 4. 조망권은 2칸이 확보되어야 하기 때문에 4개의 숫자중 제일 작은 값이 조망권을 확보한 층수이다.

# 설계
> 1. 건물의 높이를 리스트로 받아온다.
> 2. 리스트의 처음 2개의 인덱스와 마지막 2개의 인덱스는 건물이 없으므로 건너뛴다.
> 3. 뺄셈한 4개의 수를 계산한다.
> 4. 이중 음수가 한개도 없다면 새로운 리스트에 합쳐주고 최솟값을 가져온다.
> 5. 가져온 최솟값을 기존 조망권 층수에 합산하여 계산

'''

T = 10
for test_case in range(1, T + 1):

    n = int(input())
    arr = list()
    sol = 0
    arr = list(map(int, input().split()))
    # print(arr)

    for i in range(n):
        if i < 2 or i > n-3:
            continue
            print(i)
        else:
            # print(arr[i])
            # print(arr[(i-1)])
            # print(arr[(i-2)])
            l1 = arr[i] - arr[i-1]
            r1 = arr[i] - arr[i+1]
            l2 = arr[i] - arr[i-2]
            r2 = arr[i] - arr[i+2]
            # print(l2, l1, r1, r2)

            if l1 > 0 and r1 > 0 and l2 > 0 and r2 > 0:
                arr2 = list()
                arr2.append(l1)
                arr2.append(r1)
                arr2.append(l2)
                arr2.append(r2)
                # print(f"min(arr2) : {min(arr2)}")
                sol = sol + min(arr2)
    print(sol)