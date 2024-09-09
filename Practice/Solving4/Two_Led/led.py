import sys
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
results = [0] * t
for test_case in range(t):
    a, b, c, d = map(int, input().split())
    result = min(b, d) - max(a, c)
    if result < 0:
        results[test_case] = 0
        continue
    results[test_case] = result

for i in range(t):
    print(f"#{i + 1} {results[i]}")