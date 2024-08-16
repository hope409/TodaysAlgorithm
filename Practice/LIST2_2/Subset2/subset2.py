import sys
sys.stdin = open('input.txt')

def find_subset(n, arr): # n : 부분집합을 구할 집합의 원소의 개수 // arr : 전체집합
    global number, bit, subset_li  # number : 전체집합의 원소의 개수
                                   # bit : 원소의 상태를 나타낸 리스트
                                   # subset_li : 부분집합들을 모아둔 리스트
    if n == 1: # 마지막 원소의 상태 구분단계
        bit[0] = 0
        subset_li.append([bit[i] * arr[i] for i in range(number)])
        bit[0] = 1
        subset_li.append([bit[i] * arr[i] for i in range(number)])

    else: # 첫번째 원소 ~ 마지막 직전까지 구분
        bit[n - 1] = 0
        find_subset(n - 1, arr)
        bit[n - 1] = 1
        find_subset(n - 1, arr)

        # return subset_li # 할당을 안해 줬기 때문에 맨 처음의 리턴값만 가져오는 것이 가능

def sum_arr(arr):
    result = 0
    for elem in arr:
        result += elem
    return result

t = int(input())
for test_case in range(1, t + 1):
    arr = list(map(int, input().split()))
    number = len(arr)  # number : 전체집합의 원소의 개수
    bit = [0] * number  # bit : 원소의 상태를 나타낸 리스트
    subset_li = list()  # subset_li : 부분집합들을 모아둔 리스트

    find_subset(number, arr) # subset_li 갱신

    status = 0 # 출력할 결과 값
    for sub in subset_li[1:]: # 공집합을 제외하고 시작
        if sum_arr(sub) == 0:
            status = 1
            break

    print(f"#{test_case} {status}")