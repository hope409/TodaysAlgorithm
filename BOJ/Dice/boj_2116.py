import copy
def dice_sum(arr, num): # 주사위 목록 / 제외할 숫자
    dices = copy.deepcopy(arr)
    sum_all = 0
    pre_num = num
    for dice in dices:
        for idx in range(6):
            if dice[idx] == pre_num:
                pre_idx = idx
                break
        if pre_idx == 0 or pre_idx == 5:  # 다음 인덱스 찾아가기
            next_idx = 5 - pre_idx
        elif pre_idx == 1 or pre_idx == 3:
            next_idx = 4 - pre_idx
        elif pre_idx == 2 or pre_idx == 4:
            next_idx = 6 - pre_idx

        a = dice[pre_idx] # 위아래 오는 것들 삭제
        pre_num = dice.pop(next_idx)
        dice.remove(a)
        sum_all += max(dice)
    return sum_all


n = int(input()) # 주사위의 개수
dice_li = [list(map(int, input().split())) for _ in range(n)] # 주사위 목록 받기
max_sum = 0
for i in range(1, 7): # 맨밑에 오는 숫자 1~6 경우 다 해보기
    pre_sum = dice_sum(dice_li, i)
    if pre_sum > max_sum:
        max_sum = pre_sum
print(max_sum)