import sys
sys.stdin = open('input.txt')

def sort_down(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
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
        num_li = sort_down(num_li)
        num_li[0] = num_li[0] - 1
        num_li[-1] = num_li[-1] + 1
    print(f"#{test_case} {max(num_li) - min(num_li)}")