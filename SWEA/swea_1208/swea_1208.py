'''

# SWEA 1208번

# 문제 해석
> 1. 가로의 길이는 100이다.
> 2. 덤프의 크기만큼 상자를 움직일 수 있다.
> 3. 주어진 숫자는 상자가 쌓여있는 갯수이다.
> 4. 움직여서 최대값과 최소값의 차를 구한다.

# 발상
> 1. 오름차순 혹은 내림차순 정렬을 한다.
> 2. 양쪽 끝에서 한쪽은 1을 차감 한쪽은 1을 가한다.
> 3. 1, 2를 덤프의 수만큼 반복한다.
> 4. 반복문이 끝난 후 최대 최소의 차를 구한다.

# 설계
> 1. 덤프의 수 그리고 상자높이는 리스트로 받아온다.
> 2. 내림차순 정렬해준다.

'''
import sys
sys.stdin = open('input.txt')
def sort_up(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 덤프의 수
    n = int(input())
    # 상자높이 리스트 가져오기
    num_li = list(map(int, input().split()))
    # 덤프 횟수만큼 정렬하면서 상자 옮기기
    for i in range(n):
        num_li.sort(reverse=True)
        print(num_li)
        num_li[0] = num_li[0] - 1
        num_li[-1] = num_li[-1] + 1
    print(f"#{test_case} {max(num_li) - min(num_li)}")