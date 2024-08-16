import sys
sys.stdin = open('sample_input.txt')

def paper(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return paper(N-10) + paper(N-20) * 2

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    print(f"#{test_case} {paper(n)}")
