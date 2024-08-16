import sys
sys.stdin = open('sample_input.txt')

def BruteForce(pat, text):
    N = len(text)
    M = len(pat)
    i = 0  # text의 인덱스
    j = 0  # 패턴의 인덱스
    cnt = 0 # text에 있는 패턴의 수

    while j < M and i < N:

        # 틀린 곳을 발견했다면, index 값을 초기화 시킴.
        if text[i] != pat[j]:
            # text의 현재 위치에서 일치하지 않는 곳을 발견!
            #  지금위치 - j
            i = i - j
            j = - 1

        i = i + 1
        j = j + 1

        # 검색 성공
        if j == M:
            j = 0
            cnt += 1
    return cnt

# def BruteForceV2(pat, text):
#     cnt = 0
#     for idx in range(len(text) - len(pat) + 1):
#         # 패턴을 처음부터 끝까지 순회
#         for j in range(len(pattern)):

#             # 1. 다르면, break
#             if text[idx + j] != pat[j]:
#                 break
#         # 같다면(다른게 없다면)
#         else:
#             cnt += 1
#     return cnt

t = int(input())
for test_case in range(1, t + 1):
    text, pattern = input().split()

    cnt = BruteForce(pattern, text)
    print(cnt)
    print(f"#{test_case} {len(text) - (len(pattern) - 1)*cnt}")



    T = int(input())

for tc in range(1,T+1):
    data = input()
    
    ans = 0
    cnt = 0
    stack = []
    
    for elm in data:    
        if elm == '(':
            cnt += 1
        elif elm == ')':
            if stack != [] and stack[-1] == '(':
                cnt -= 1
                ans += cnt
            else:
                stack.pop()
                ans += 1
                cnt -= 1
        stack.append(elm)
    print(f'#{tc} {ans}')
