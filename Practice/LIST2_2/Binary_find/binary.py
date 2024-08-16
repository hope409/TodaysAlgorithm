import sys
sys.stdin = open('sample_input.txt')

def binary_find(s_page, f_page): # 이진탐색
    cnt, center, left, right = 0, 0, 1, s_page

    while center != f_page:
        center = (left + right) // 2
        cnt += 1
        if center < f_page: # 왼쪽 잘라내기
            left = center
        elif center > f_page: # 오른쪽 잘라내기
            right = center
        else:               # 찾음
            return cnt

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 테스트케이스 시작
    page, a, b = map(int, input().split()) # 총페이지 // A가 찾을쪽 // B가 찾을쪽

    cnt_a = binary_find(page, a) # A 탐색
    cnt_b = binary_find(page, b) # B 탐색

    if cnt_a < cnt_b:
        print(f"#{test_case} A")
    elif cnt_a > cnt_b:
        print(f"#{test_case} B")
    else:
        print(f"#{test_case} 0")