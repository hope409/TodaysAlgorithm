# from itertools import combinations
#
# n, k = map(int, input().split())
# max_count = 0
# readable_default = 0
# if k < 5:
#     print(max_count)
# else:
#     default = ['a', 'n', 't', 'i', 'c']
#     word_list = [[] for _ in range(n)]
#     for i in range(n):
#         alpa_list = []
#         word = input()[4:-4]
#         for alpa in word:
#             if alpa not in default:
#                 alpa_list.append(alpa)
#         if len(alpa_list) > k - 5:
#             continue
#         elif not alpa_list:
#             readable_default += 1
#         else:
#             word_list[i] = alpa_list
#     # all_used = set(sum(word_list, []))
#     all_used = set([alpa for case in word_list for alpa in case])
#     if not all_used:
#         print(readable_default)
#     else:
#         subset_list = list(combinations(list(all_used), k - 5))
#         for subset in subset_list:
#             count = 0
#             for case in word_list:
#                 if not case:
#                     continue
#                 for element in case:
#                     if element not in subset:
#                         break
#                 else:
#                     count += 1
#             if count > max_count:
#                 max_count = count
#         print(max_count + readable_default)

from itertools import combinations

n, k = map(int, input().split())
max_count = 0
readable_default = 0

if k < 5:
    print(0)  # 기본 문자 5개도 배울 수 없으면 아무 단어도 읽을 수 없음
else:
    default = ['a', 'n', 't', 'i', 'c']
    word_list = []

    for i in range(n):
        word = input()[4:-4]  # 'anta'와 'tica'를 제거하고 중간 부분만 추출
        alpa_list = [alpa for alpa in word if alpa not in default]  # 기본 문자 제외한 문자 추출

        if len(alpa_list) > k - 5:  # 배울 수 있는 문자의 개수를 초과하면 건너뛰기
            continue
        elif not alpa_list:  # 기본 문자로만 이루어진 경우
            readable_default += 1
        else:
            word_list.append(alpa_list)  # 나머지 단어 저장

    all_used = set([alpa for case in word_list for alpa in case])  # 모든 사용된 문자 추출

    if not all_used:  # 배워야 할 문자가 없는 경우
        print(readable_default)  # 기본 문자만으로 읽을 수 있는 단어 수 출력
    else:
        # 배울 수 있는 문자들의 조합을 생성 (k-5 개 선택)
        subset_list = list(combinations(all_used, k - 5))

        for subset in subset_list:
            count = 0
            for case in word_list:
                if all(alpa in subset for alpa in case):  # 해당 부분집합으로 읽을 수 있는지 확인
                    count += 1
            max_count = max(max_count, count)

        # 기본 문자만으로 읽을 수 있는 단어 수를 더해 최종 출력
        print(max_count + readable_default)
