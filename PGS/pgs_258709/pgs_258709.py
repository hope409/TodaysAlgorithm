# 케이스 18번까지 5개 틀림
# 그뒤는 시간초과

import numpy as np
import itertools


def simulate_dice_rolls(dices, trials=10000):
    results = [0] * 10000
    for i in range(trials):
        rolls = [np.random.choice(select_dice) for select_dice in dices]  # 각 주사위에서 무작위로 한 번 던진 결과
        results[i] = sum(rolls)  # 총합을 계산
    return np.mean(results)  # 평균 점수를 반환


def solution(dice):
    n = len(dice)  # 주사위의 개수
    num_to_select = n // 2  # 선택할 주사위 개수

    best_average = -1  # 최고의 평균 점수
    best_combination = None  # 최고의 조합

    # 가능한 모든 주사위 선택 조합을 구함
    for combination in itertools.combinations(range(n), num_to_select):
        selected_dice = [dice[i] for i in combination]  # 선택된 주사위
        average_score = simulate_dice_rolls(selected_dice)  # 평균 점수 계산

        # 가장 높은 평균 점수를 찾음
        if average_score > best_average:
            best_average = average_score
            best_combination = combination

    # 가장 좋은 조합을 answer에 저장 (주사위의 인덱스 + 1)
    answer = [i + 1 for i in best_combination]  # 인덱스에 1을 더함

    return answer