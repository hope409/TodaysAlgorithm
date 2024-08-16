import sys
sys.stdin = open('input.txt')


t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n, k = map(int, input().split()) # n : 퍼즐 크기 / k : 단어 길이
    puzzle = [list(input().split()) for _ in range(n)] # 퍼즐 그리기
    p_li = [] # 칸수 구분해서 넣기
    for i in range(n):
        a = ''
        b = ''
        for j in range(n):
            a += puzzle[i][j] # 가로탐색
            b += puzzle[j][i] # 세로탐색
        p_li.append(a.split('0')) # 0제외하고 1의 모음
        p_li.append(b.split('0'))
    cnt = 0
    for li in p_li:
        for string in li:
            if len(string) == k:
                cnt += 1
    print(f"#{test_case} {cnt}")
