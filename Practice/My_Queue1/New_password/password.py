import sys
sys.stdin = open('input.txt')

t = 10 # 테스트 케이스 개수
for test_case in range(1, t + 1): # 시작
    tc = int(input()) # 테스트케이스 번호
    password = list(map(int, input().split())) # 비밀번호 리스트
    cnt = 1 # 뺄셈할 수
    front = -1
    while True:
        front = (front + 1) % 8 # 자리 이동해주기

        if password[front] <= cnt: # 비밀번호 구하기 마지막 단계
            password[front] = 0
            break

        password[front] -= cnt # 현재 주기 계산
        cnt += 1 # 다음 주기로 이동

        if cnt == 6: # 한 사이클 끝
            cnt = 1
    # 1. 비밀번호 순서 찾기 / 리스트컴프리헨션
    # idx_li = [x % 8 for x in range(front + 1, front + 9)]


    # 2. 비밀번호 순서 찾기 / 반복문을 사용한 경우
    idx_li = list()
    for x in range(front + 1, front + 9):
        idx_li.append(x % 8)


    print(f"#{tc}", end= ' ') # 출력
    for idx in idx_li:
        print(password[idx], end= ' ')
    print()
