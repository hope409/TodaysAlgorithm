import sys
sys.stdin = open('input.txt')

def find_not_zero(arr):
    for i in range(n):
        if arr[i] != 0:
            return i

def count_zero(arr):
    cnt = 0
    for elem in arr:
        if elem == 0:
            cnt = cnt + 1
    return  cnt

def subtract_one(arr):
    for i, elem in enumerate(arr):
        if elem > 0:
            arr[i] = elem - 1
    return arr

# t = int(input())
# for test_case in range(1, t + 1):
#     n = int(input())
#     box_li = list(map(int, input().split()))
#     max_cnt = 0
#     for _ in range(max(box_li) - 1):
#         position = find_not_zero(box_li)
#         count = count_zero(box_li)
#         pre_cnt = n - position - count
#         if max_cnt < pre_cnt:
#             max_cnt = pre_cnt
#         box_li = subtract_one(box_li)
#
#     print(f"#{test_case} {max_cnt}")

t = int(input())

# t 번만큼 순회
for test_case in range(1, t + 1):
    # 상자들이 담겨있는 칸의 개수
    n = int(input())
    # 각상자들의 높이가 담겨있다.
    # 공백을 기준으로 입력받는다.
    num_arr = list(map(int, input().split()))  # [7, 4, 2, 0, 0, 6, 0, 7, 0]

    result = 0  # 최종 결과값

    # 모든 상황에 대한 낙차값 구하기 위해 순회
    for i in range(n):
        # 방해를 받지 않았을 때, i번째 상자가 떨어질 수 있는 최대 높이
        # 전체길이 - 내 위치 + 1
        max_h = len(num_arr) - (i + 1)

        # 내 다음으로 오는 상자 중 나와 높이가 같거나 더 큰 박스 찾기
        for j in range(i + 1, len(num_arr)):
            # i 와 j를 비교 -> i는 현재 검사중인 박스, j는 내 오른쪽에 있는 박스들을 순차 검사
            if num_arr[i] <= num_arr[j]:
                max_h -= 1

        # 여기서, 지금 검사한 상자 높이가 result 값보다 크다면 갱신
        if result < max_h:
            result = max_h

    print(f'#{test_case} {result}')

