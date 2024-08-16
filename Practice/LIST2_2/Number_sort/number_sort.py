import sys
sys.stdin = open('input.txt')

def sort_down(n, arr): # 오름차순 거품정렬
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

t = int(input()) # 테스트 케이스 개수
for test_case in range(1, t + 1): # 테스트케이스 시작
    n = int(input()) # 숫자열 개수
    num_arr = list(map(int, input().split())) # 숫자열
    sort_arr = sort_down(n, num_arr)
    print(f"#{test_case}", end= ' ')
    print(*sort_arr)
