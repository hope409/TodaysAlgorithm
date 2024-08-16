'''
# SWEA 1209번

# 문제 해석
> 1. 배열의 크기는 100x100
> 2. 행, 열, 대각선의 합중 최대값을 찾는다.
> 3. 입력으로는 테스트케이스 번호, 1행부터의 값이 주어진다.

# 발상
> 1. 

# 설계
> 1. 

'''

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    arr = list()
    sum_li = list()
    for i in range(100):
        i_col = list(map(int, input().split()))
        arr.append(i_col)

    # 행별 합 구하기
    for col in range(100):
        val = 0
        for row in range(100):
            val = val + arr[col][row]
        sum_li.append(val)
    
    # 열별 합 구하기
    for row in range(100):
        val = 0
        for col in range(100):
            val = val + arr[col][row]
        sum_li.append(val)
    
    # 대각선 합 구하기
    val = 0
    val2 = 0
    for idx in range(100):
        val = val + arr[idx][99-idx]
        val2 = val2 + arr[idx][idx]
    sum_li.append(val)
    sum_li.append(val2)

    # 결과 출력
    print(f"#{num} {max(sum_li)}")