# def solution(clothes):
#     answer = 1
#     costumes = dict()
#     for name, cloth_type in clothes:
#         if cloth_type in costumes.keys():
#             costumes[cloth_type] += 1
#         else:
#             costumes[cloth_type] = 1
#     for cnt in costumes.values():
#         answer *= cnt + 1
#     return answer - 1

from collections import defaultdict
import math
def solution(clothes):
    costumes = defaultdict(lambda :1)
    for name, cloth_type in clothes:
        costumes[cloth_type] += 1
    answer = math.prod(costumes.values()) - 1
    return answer