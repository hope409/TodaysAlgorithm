t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    a, b = map(int, input().split()) # a : 나누어지는 수
    c = a // b # 몫 계산
    d = a % b # 나머지 계산
    print(f"#{test_case} {c} {d}")