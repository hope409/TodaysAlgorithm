import sys
sys.stdin = open('sample_input.txt')

def divide_sort(root_li): # 분할하기
    if len(root_li) == 1: # 분할대상이 1개일때
        return root_li
    # 분할대상이 2개 이상일 때
    middle = len(root_li) // 2 # 중간값 찾기 
    left_li, right_li = root_li[:middle], root_li[middle:] # 왼쪽 오른쪽 분할
    
    # 각각을 다시 분할
    left_li = divide_sort(left_li)
    right_li = divide_sort(right_li)
    
    # 병합 후 출력
    return merge(left_li, right_li)

def merge(left_li, right_li): # 병합하기
    global cnt
    result = [] # 병합결과
    # 왼쪽리스트의 오른쪽 원소가 더 클때
    if left_li[-1] > right_li[-1]:
        cnt += 1
    # 현재 비교하는 중인 인덱스 번호
    left_idx, right_idx = 0, 0

    # 병합해야 할 원소가 한개라도 남아있다면?
    while left_idx != len(left_li) or right_idx != len(right_li):
        # 둘다 남아있다면?
        if left_idx != len(left_li) and right_idx != len(right_li):
            # 오른쪽이 더 크다면?
            if left_li[left_idx] <= right_li[right_idx]:
                result.append(left_li[left_idx])
                left_idx += 1
            # 왼쪽이 더 크다면?
            else:
                result.append(right_li[right_idx])
                right_idx += 1
        # 왼쪽만 남아있다면?
        elif left_idx != len(left_li):
            result.append(left_li[left_idx])
            left_idx += 1
        # 오른쪽만 남아있다면?
        elif right_idx != len(right_li):
            result.append(right_li[right_idx])
            right_idx += 1
    return result

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 정수의 개수
    num_li = list(map(int, input().split()))
    cnt = 0
    num_li = divide_sort(num_li)
    print(f"#{test_case} {num_li[n//2]} {cnt}")
