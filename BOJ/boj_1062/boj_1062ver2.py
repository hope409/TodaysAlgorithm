from itertools import combinations

def teaching(n, k, words):
    max_count = 0
    readable_default = 0
    # 기본 글자 5개도 배울 수 없으면 아무 단어도 읽을 수 없음
    if k < 5:
        return 0

    # 배울 수 있는 글자 수에서 기본 글자 5개를 뺀 나머지 글자 수
    can_learn = k - 5

    # 모든 단어에서 기본 글자를 제외하고 필요한 글자들만 추출
    learnable_set = set()
    filtered_words = []

    for word in words:
        filtered_word = word - default
        if filtered_word:  # 기본 글자만 남은 단어는 배울 필요 없음
            filtered_words.append(filtered_word)
            learnable_set.update(filtered_word)
        else:
            readable_default += 1

    # 만약 배워야 할 글자의 종류가 배울 수 있는 글자 수보다 적으면 모든 단어를 읽을 수 있음
    if len(learnable_set) <= can_learn:
        return n

    # 배워야 할 글자 조합 중에서 최대한 많은 단어를 읽을 수 있는 경우를 탐색
    for comb in combinations(learnable_set, can_learn):
        learned_set = set(comb)
        count = readable_default
        for word in filtered_words:
            if word.issubset(learned_set):  # 배운 글자들로 해당 단어를 읽을 수 있는지 확인
                count += 1
        max_count = max(max_count, count)

    return max_count

n, k = map(int, input().split())  # 단어의 개수 / 배울 수 있는 글자의 개수
words = [set(input()) for _ in range(n)]  # 각 단어를 입력 받아서 set으로 변환
default = {'a', 'n', 't', 'i', 'c'}  # 기본적으로 알아야 하는 글자
print(teaching(n, k, words))