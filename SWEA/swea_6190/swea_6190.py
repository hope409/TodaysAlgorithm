'''
# SWEA 6190번

# 문제 해석
> 1. 단조 증가하는 수란 가장 높은 자리수 부터 단순히 증가하는 수 ex) 1234, 11222
> 2. 주어진 숫자들의 단순 곱을 전부 계산한다.
> 3. 각각의 계산된 숫자의 자리수가 단순히 증가하는지 확인한다.
> 4. 이때 한자리 숫자는 단조 증가하는 수가 아니다.

# 발상
> 1. 단순곱의 리스트를 내림차순 정렬한다.
> 2. 0번 인덱스 부터 비교하면 처음 나온 단조 증가수가 최대값이다.
> 3. 각 자리숫자를 가져올때 일의 자리수부터 순서대로 가져온다.
> 4. 이때 자리숫자를 저장한 리스트가 내림차순한 리스트와 순서가 같으면 단조 증가이다.

# 설계
> 1. 단순 곱의 결과를 리스트에 저장하고 내림차순 정렬한다.
> 2. 각 자리숫자를 리스트에 저장하고 내림차순 정렬한다.

'''

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    li = list()

    # 단순 곱 계산
    for i in range(N):
        j = i + 1
        while j < N : 
            li.append(num_list[i] * num_list[j])
            j = j + 1

    # 계산한 수를 내림차순 정렬
    li.sort(reverse=True)
    cnt = 0 # 단조 증가 하는 수를 찾았는지 확인하는 수
    val = 0 # 단조 증가 수 중에서 가장 큰 수
    for num in li:
        # 단조 증가수를 찾았다면 반복문을 탈출
        if cnt != 0:
            break
        # 각 자리숫자를 찾아서 리스트에 저장
        arr = list()
        num2 = num
        while num2 != 0:
            a = num2 % 10
            num2 = num2 // 10
            arr.append(a)
        # 한자리 숫자이면 단조 증가가 아니므로 패스
        if len(arr) == 1:
            continue
        # 각 자리숫자를 저장한 리스트를 내림차순으로 정렬
        arr2 = sorted(arr, reverse=True)
        for i in range(len(arr)):
            # 내림차순 한 것과 다르면 단조 증가가 아님
            if arr[i] != arr2[i]:
                break
            # 단조 증가수를 찾는 곳
            if i == len(arr) - 1:
                cnt = 1
                val = num
    if cnt == 0:
        print(f"#{test_case} -1")
    else:
        print(f"#{test_case} {val}")