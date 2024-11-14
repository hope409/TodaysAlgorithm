from collections import deque

def solution(coin, cards):
    cards = deque(cards) # 카드 뭉치
    number_of_cards = len(cards) # 카드의 개수
    sum_of_cards = number_of_cards + 1
    able_round = 0 # 진행 가능 라운드 수
    count_round = 1 # 현재 라운드 수
    counting_li = [0] * (number_of_cards + 1) # 손에 들고있는 카드 목록
    used = [0] * (number_of_cards + 1) # 카드 사용 여부
    counting_temp = [0] * (number_of_cards + 1) # 사용하지 않고 넘어간 카드뭉치 목록
    number_of_hands = number_of_cards // 3 # 다음에 가져올 카드의 인덱스 번호
    temp_deck = set() # 전 라운드에 사용하지 않고 넘어간 카드뭉치

    for i in range(number_of_hands):
        card = cards[i]
        counting_li[card] = 1

    for _ in range(number_of_hands): # 현재 손에 있는 카드 체크 시작
        hand = cards.popleft()
        if used[hand] == 1: # 이미 페어로 사용된 카드이면?
            continue
        pair = sum_of_cards - hand # 페어 계산
        if counting_li[pair] == 1: # 만약에 페어가 있다면?
            used[hand], used[pair] = 1, 1
            counting_li[hand], counting_li[pair] = 0, 0
            able_round += 1 # 진행가능 라운드 + 1

    # 진행 가능 라운드가 남아있는 동안 게임 지속
    while cards:
        # 코인이 있다면? 카드 가져올지 고민
        if coin and cards:
            card1, card2 = cards.popleft(), cards.popleft()
            card1_pair, card2_pair = sum_of_cards - card1, sum_of_cards - card2
            if coin and counting_li[card1_pair] == 1: # card1의 페어가 손에 있다면?
                # 사용처리 하고 다음 라운드로 이동
                used[card1_pair], used[card1] = 1, 1
                counting_li[card1_pair] = 0
                coin -= 1
                able_round += 1
            else: # card1의 페어가 손에 없으면?
                counting_temp[card1] = 1 # 덱에 임시저장했으니까 추가
                temp_deck.add(card1)

            if coin and counting_li[card2_pair] == 1: # card2의 페어가 손에 있다면?
                # 사용처리 하고 다음 라운드로 이동
                used[card2_pair], used[card2] = 1, 1
                counting_li[card2_pair] = 0
                coin -= 1
                able_round += 1
            else: # card2의 페어가 손에 없으면?
                counting_temp[card2] = 1  # 덱에 임시저장했으니까 추가
                temp_deck.add(card2)

        # 코인이 있고 진행 가능 라운드가 없다면?
        while temp_deck and coin >= 2 and not able_round:
            temp_card = temp_deck[0] # 현재 잔여카드
            if used[temp_card]:  # 이미 사용된 카드라면?
                temp_deck.popleft() # 버리기
            pair = sum_of_cards - temp_card # 해당카드의 페어
            if counting_temp[pair]: # 미사용 카드뭉치에 페어가 있다면?
                used[temp_card], used[pair] = 1, 1
                counting_temp[temp_card], counting_temp[pair] = 0, 0
                able_round += 1
                coin -= 2
        if not able_round: # 잔여라운드가 없다면
            break
        count_round += 1
        able_round -= 1

    return count_round

# print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))
# print(solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
# print(solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]))
# print(solution(3, [1, 2, 3, 4, 5, 8, 12, 10, 9, 7, 6, 11]))
print(solution(12,[1,12,2,11,3,10,4,9,5,8,6,7]))