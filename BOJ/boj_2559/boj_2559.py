n, k = map(int, input().split()) # n : 날짜의 수 / k : 연속적인 날짜의 수
num_arr = list(map(int, input().split())) # 온도의 배열
stack = [num_arr.pop(0) for _ in range(k - 1)] # 합을 계산할 리스트
top = -1
max_val = None # 최대 값을 갱신할 변수
# while num_arr:
#     stack.append(num_arr.pop(0)) # 다음 숫자 집어넣기
#     pre_val = sum(stack) # 합 구하기
#     if max_val is None: # 초기 값 할당하기
#         max_val = pre_val
#     elif pre_val > max_val: # 최대 값 갱신하기
#         max_val = pre_val
#     stack.pop(0) # 맨앞에 숫자 빼기

q = [0] * n
front = -1
rear = -1
while rear < n - 1:
    rear += 1
    q[rear] = num_arr[rear]
    if rear < k - 1:
        continue
    pre_val = sum(q)
    if max_val is None:
        max_val = pre_val
    elif pre_val > max_val:
        max_val = pre_val
    front += 1
    q[front] = 0

print(max_val)