def xnor(a, b, B):
    return ~ (a ^ b) & ((1 << B) - 1)

def max_xnor(N, B, A):
    # 입력이 하나인 경우
    if N == 1:
        return A[0]

    max_result = 0
    current_xnor = 0

    for i in range(N):
        current_xnor = xnor(current_xnor, A[i], B)
        max_result = max(max_result, current_xnor)

    return max_result

# 예시 입력
N, B = map(int, input().split())
A = list(map(int, input().split()))

# 결과 출력
result_single_input = max_xnor(N, B, A)
print(result_single_input)
print(xnor(2, 2, 3))