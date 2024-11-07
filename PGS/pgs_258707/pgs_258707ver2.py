from collections import deque

def solution(coin, cards):
    cards = deque(cards)
    number_of_cards = len(cards)
    sum_of_cards = number_of_cards + 1
    able_round = 0
    count_round = 1
    counting_li = [0] * (number_of_cards + 1)
    used = [0] * (number_of_cards + 1)
    number_of_hands = number_of_cards // 3
    hands = deque([])
    temp_deck = deque([])

    # 초기 핸드 구성
    for _ in range(number_of_hands):
        card = cards.popleft()
        counting_li[card] = 1
        hands.append(card)

    # 초기 핸드에서 가능한 페어를 만든다
    for _ in range(number_of_hands):
        hand, pair = hands[0], sum_of_cards - hands[0]
        if counting_li[pair] == 1:
            used[hand], counting_li[hand] = 1, 0
            used[pair], counting_li[pair] = 1, 0
            able_round += 1
            hands.popleft()
        elif used[hand] == 1:
            hands.popleft()
        else:
            hands.rotate(-1)

    # 진행 가능한 라운드가 있는 동안 게임 진행
    while able_round or (cards or temp_deck):
        if able_round == 0:  # 더 이상 진행할 수 있는 라운드가 없으면 탈출
            break

        count_round += 1
        able_round -= 1

        # 임시 덱에서 페어를 찾는다
        for _ in range(len(temp_deck)):
            card = temp_deck.popleft()
            pair = sum_of_cards - card
            if counting_li[pair] == 1:  # 페어가 있으면 사용
                used[card], used[pair] = 1, 1
                counting_li[card], counting_li[pair] = 0, 0
                able_round += 1
            else:
                hands.append(card)  # 페어가 없으면 손에 넣음

        # 코인 사용 시 최적 페어 탐색
        if coin > 0 and cards:
            card1, card2 = cards.popleft(), cards.popleft()
            card1_pair, card2_pair = sum_of_cards - card1, sum_of_cards - card2

            # card1의 페어가 있는 경우
            if counting_li[card1_pair] == 1:
                used[card1_pair], counting_li[card1_pair] = 1, 0
                used[card1] = 1
                coin -= 1
                able_round += 1
            else:
                temp_deck.append(card1)  # 페어가 없는 경우 임시 덱에 추가

            # card2의 페어가 있는 경우
            if counting_li[card2_pair] == 1:
                used[card2_pair], counting_li[card2_pair] = 1, 0
                used[card2] = 1
                coin -= 1
                able_round += 1
            else:
                temp_deck.append(card2)  # 페어가 없는 경우 임시 덱에 추가

    return count_round

# 테스트
result = solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])
print(result)  # 예상 결과: 5
