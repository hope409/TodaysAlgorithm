num = int(input()) # 끝 숫자

for i in range(1, num + 1):             # 1~num까지
    three_number_li = []
    pre_num = i                         # 연산에 사용할 현재 숫자
    while pre_num != 0:                          # 각 자리수 분리과정
        pre = pre_num % 10                            # 현재 일의 자리
        if pre == 3 or pre == 6 or pre == 9:                        # 3의배수라면?
            three_number_li.append(pre)
        pre_num //= 10                              # 일의자리를 버린 후의 숫자
    if three_number_li:                     # 3, 6, 9가 있었다면? 그 개수만큼 출력
        print('-' * len(three_number_li), end= ' ')
    else:                                   # 아니라면 그냥 숫자 출력
        print(i, end= ' ')
print()                                         # 마지막 줄 바꿈