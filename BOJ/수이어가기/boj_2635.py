'''
100

8
100 62 38 24 14 10 4 6
'''

first_num = int(input()) # 첫번째 숫자
max_li = [first_num]
max_len = len(max_li)
for second_num in range(first_num//2, first_num + 1): # 처음 수의 절반보다 작은 수면 바로 끝남
    pre_li = [first_num, second_num] # 최대 길이 목록
    pre_len = 0
    while True:
        next_num = pre_li[-2] - pre_li[-1] # 다음꺼 = 전전꺼 - 전꺼
        if next_num < 0: # 0보다 작은지 확인
            pre_len = len(pre_li)
            if pre_len > max_len:
                max_len = pre_len
                max_li = pre_li
            break
        pre_li.append(next_num)

print(max_len)
print(*max_li)