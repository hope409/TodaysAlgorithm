import sys
sys.stdin = open('sample_input.txt')

def quick_sort(left, right): # 리스트, 왼쪽, 오른쪽
    if left < right:
        section = partition(left, right)
        quick_sort(left, section - 1)
        quick_sort(section + 1, right)

def partition(left, right):
    pivot = li[left]
    i, j = left + 1, right
    while i <= j:
        while i <= j and li[i] <= pivot:
            i += 1
        while i <= j and li[j] >= pivot:
            j -= 1
        if i < j:
            li[i], li[j] = li[j], li[i]
    li[left], li[j] = li[j], li[left]
    return j

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 정수의 개수
    li = list(map(int, input().split()))
    quick_sort(0, n - 1)
    print(f"#{test_case} {li[n//2]}")