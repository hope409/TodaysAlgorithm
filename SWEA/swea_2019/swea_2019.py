num = int(input()) # 지수
mul_val = 1 # 곱
for i in range(1, num + 1): # 곱셈 시작
    print(mul_val, end= ' ') # 곱셈 전 출력
    mul_val *= 2
print(mul_val) # 마지막 계산 후 출력