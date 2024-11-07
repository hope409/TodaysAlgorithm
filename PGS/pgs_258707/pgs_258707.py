from collections import deque

def solution(coin, cards):
    cards = deque(cards) # 카드 뭉치
    number_of_cards = len(cards) # 카드의 개수
    sum_of_cards = number_of_cards + 1
    able_round = 0 # 진행 가능 라운드 수
    count_round = 1 # 현재 라운드 수
    counting_li = [0] * (number_of_cards + 1) # 손에 들고있는 카드 목록
    used = [0] * (number_of_cards + 1) # 카드 사용 여부
    number_of_hands = number_of_cards // 3 # 다음에 가져올 카드의 인덱스 번호
    hands = deque([]) # 손에 들고있는 카드뭉치
    temp_deck = deque([]) # 전 라운드에 사용하지 않고 넘어간 카드뭉치

    for _ in range(number_of_hands):
        card = cards.popleft()
        counting_li[card] = 1
        hands.append(card)

    for _ in range(number_of_hands): # 현재 손에 있는 카드 체크 시작
        hand, pair = hands[0], sum_of_cards - hands[0]
        # if hand == pair: # 자기 자신이 페어라면 패스
        #     hands.rotate(-1)
        #     continue
        if counting_li[pair] == 1: # 만약에 페어가 있다면?
            used[hand], counting_li[hand] = 1, 0
            used[pair], counting_li[pair] = 1, 0
            able_round += 1 # 진행가능 라운드 + 1
            hands.popleft()
        elif used[hand] == 1: # 이미 페어로 사용된 카드이면?
            hands.popleft()
        else: # 페어가 없는 카드면 다음 카드 확인
            hands.rotate(-1)
    # 진행 가능 라운드가 남아있는 동안 게임 지속
    while able_round and cards:
        count_round += 1
        able_round -= 1
        # 코인이 있다면? 카드 가져올지 고민
        if coin and cards:
            card1, card2 = cards.popleft(), cards.popleft()
            card1_pair, card2_pair = sum_of_cards - card1, sum_of_cards - card2
            if coin and counting_li[card1_pair] == 1: # card1의 페어가 손에 있다면?
                # 사용처리 하고 다음 라운드로 이동
                used[card1_pair], counting_li[card1_pair] = 1, 0
                used[card1] = 1
                coin -= 1
                able_round += 1
                continue
            else: # card1의 페어가 손에 없으면?
                temp_deck.append(card1)
                # counting_li[card1] = 1 # 덱에 임시저장했으니까 일단 추가

            if coin and counting_li[card2_pair] == 1: # card2의 페어가 손에 있다면?
                # 사용처리 하고 다음 라운드로 이동
                used[card2_pair], counting_li[card2_pair] = 1, 0
                used[card2] = 1
                coin -= 1
                able_round += 1
                continue
            else: # card2의 페어가 손에 없으면?
                temp_deck.append(card2)
                # counting_li[card2] = 1 # 덱에 임시저장했으니까 일단 추가

    return count_round

# result = solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])
result2 = solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
print(result2)