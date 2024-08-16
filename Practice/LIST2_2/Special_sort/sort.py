import sys
sys.stdin = open('sample_input.txt')

def sort_down(n, arr): # 내림차순 정렬(버블 정렬)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num_li = list(map(int, input().split()))
    num_li = sort_down(n, num_li)
    large_li = list() # 큰쪽 넣을 리스트
    small_li = list() # 작은쪽 넣을 리스트

    for idx in range(n):
        if idx < n / 2:
            large_li.append(num_li[idx]) # 리스트를 반으로 나누어서 큰쪽
        else:
            small_li.append(num_li[idx]) # 작은쪽
    # print(f"large_li : {large_li}")
    # print(f"small_li : {small_li}")

    num = 0
    small_li_len = len(small_li)
    for elem in small_li: # 작은쪽의 가장 큰 원소부터 맨 오른쪽에 삽입
        if num == 0:
            large_li.append(elem)
        else:
            large_li.insert(small_li_len - num, elem)
        num = num + 1

    # print(f"#{test_case} {' '.join(map(str, large_li[0:10]))}")
    print(f"#{test_case}", end= ' ')
    print(*large_li[0:10])