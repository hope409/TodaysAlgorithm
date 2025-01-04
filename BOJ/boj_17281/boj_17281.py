'''
2
4 0 0 0 0 0 0 0 0
4 0 0 0 0 0 0 0 0
'''
# n = int(input()) # 이닝의 수
# hitter_li = [list(map(int, input().split())) for _ in range(n)] # 타자들의 각 이닝별 행동
# pre_num = 0 # 현재 출전할 타자 번호(인덱스번호)
# pas_num = 0 # 마지막으로 홈에 들어온 타자 번호(인덱스번호)
# score = 0 # 현재 점수
# for hit in hitter_li: # 첫번째 이닝부터 시작
#     pas_num = pre_num # 첫번째 타자 설정
#     out_cnt = 0 # 아웃카운트 리셋
#     base_li = [0] * 9 # 각 타자 번호별 현재 위치 / 0: 홈, 1: 1루, 2: 2루, 3: 3루
#     while out_cnt != 3: # 아웃카운트가 3이되면 해당 이닝 종료
#         if hit[pre_num] == 0: # 아웃카운트 하나 증가 후 다음타자
#             out_cnt += 1
#             pre_num = (pre_num + 1) % 9  # 아웃될 때까지 계속 순환
#             continue
#         elif hit[pre_num] == 4: # 홈런을 쳤을때
#             score += 10 - base_li.count(0)
#             base_li = [0] * 9 # 베이스 리셋
#             pre_num = (pre_num + 1) % 9  # 아웃될 때까지 계속 순환
#             pas_num = pre_num
#             continue
#         base_li[pre_num] += hit[pre_num] # 타자 베이스로 이동
#         idx = pas_num # 가장 앞에 있는 주자 번호
#         while idx != pre_num: # 주자들 전체
#             if base_li[idx] == 0: # 아웃된 타자라면
#                 pas_num = (pas_num + 1) % 9 # 다음 주자 탐색
#                 continue
#
#             base_li[idx] += hit[pre_num] # 해당 베이스만큼 이동
#             if base_li[idx] >= 4: # 홈에 들어왔다면?
#                 base_li[idx] = 0 # 홈으로 복귀
#                 score += 1
#                 pas_num = (pas_num + 1) % 9
#             idx = (idx + 1) % 9
#         pre_num = (pre_num + 1) % 9 # 아웃될 때까지 계속 순환
#
# print(score) # 점수 출력

####################################################################################
from itertools import permutations
from collections import deque

n = int(input()) # 이닝의 수
# 각 이닝별 타자들의 타점
hitter_li = [list(map(int, input().split())) for _ in range(n)]
# 타순 생성
batting_order = [list(order[:3]) + [0] + list(order[3:]) for order in permutations(range(1, 9), 8)]
max_point = 0
for order in batting_order:
    # 그라운드 초기화
    ground = deque([0] * 4) # 홈, 1루, 2루, 3루
    # 첫번째 타자 인덱스 번호 초기화
    hitter_index = 0
    # 현재 타순의 점수
    cur_point = 0
    for hit in hitter_li:
        # 매 이닝마다 그라운드 초기화
        ground = deque([0] * 4)
        out_cnt = 0
        # 아웃카운트가 3개가 되기 전까지 반복
        while out_cnt < 3:
            active = hit[order[hitter_index]]
            # 안타를 친 타자라면?
            if active:
                # 타자가 타석에 진입
                ground[0] = 1
                for _ in range(active):
                    ground.rotate(1)
                    # 1루씩 진루하면서 홈에 도착하면 점수 증가
                    if ground[0]:
                        ground[0] = 0
                        cur_point += 1
            # 아웃당했다면?
            else:
                out_cnt += 1
            # 다음타자 호출
            hitter_index = (hitter_index + 1) % 9
    # 최대 득점인 경우 갱신
    if cur_point > max_point:
        max_point = cur_point

print(max_point)

########################################################################################

# from itertools import permutations
#
# n = int(input()) # 이닝의 수
# # 각 이닝별 타자들의 타점
# hitter_li = [list(map(int, input().split())) for _ in range(n)]
# # 타순 생성
# batting_order = [list(order[:3]) + [0] + list(order[3:]) for order in permutations(range(1, 9), 8)]
# max_point = 0
# for order in batting_order:
#     # 그라운드 초기화
#     ground = [0] * 4 # 홈, 1루, 2루, 3루
#     # 첫번째 타자 인덱스 번호 초기화
#     hitter_index = 0
#     # 현재 타순의 점수
#     cur_point = 0
#     for hit in hitter_li:
#         # 매 이닝마다 그라운드 초기화
#         ground = [0] * 4
#         out_cnt = 0
#         # 아웃카운트가 3개가 되기 전까지 반복
#         while out_cnt < 3:
#             active = hit[order[hitter_index]]
#             # 안타를 친 타자라면?
#             if active:
#                 # 타자가 타석에 진입
#                 ground[0] = 1
#                 # 주자 진루
#                 for i in range(3, -1, -1):
#                     # 해당 루에 주자가 있었다면
#                     if ground[i]:
#                         if i + active >= 4:
#                             cur_point += 1
#                         else:
#                             ground[i + active] = 1
#                         ground[i] = 0
#             else:
#                 out_cnt += 1
#             # 다음타자 호출
#             hitter_index = (hitter_index + 1) % 9
#     # 최대 득점인 경우 갱신
#     max_point = max(max_point, cur_point)
#
# print(max_point)

############################################################################################################

from itertools import permutations

n = int(input()) # 이닝의 수
# 각 이닝별 타자들의 타점
hitter_li = [list(map(int, input().split())) for _ in range(n)]
# 타순 생성
batting_order = [list(order[:3]) + [0] + list(order[3:]) for order in permutations(range(1, 9), 8)]
max_point = 0
for order in batting_order:
    # 그라운드 초기화
    ground = [0] * 4 # 홈, 1루, 2루, 3루
    # 첫번째 타자 인덱스 번호 초기화
    hitter_index = 0
    # 현재 타순의 점수
    cur_point = 0
    for hit in hitter_li:
        # 매 이닝마다 그라운드 초기화
        ground = [0] * 4
        out_cnt = 0
        # 아웃카운트가 3개가 되기 전까지 반복
        while out_cnt < 3:
            active = hit[order[hitter_index]]
            # 홈런일때?
            if active == 4:
                cur_point += ground.count(1) + 1
                ground = [0] * 4
            # 안타일때?
            elif active:
                # 타자가 타석에 진입
                ground[0] = 1
                # 주자 진루
                for i in range(3, -1, -1):
                    # 해당 루에 주자가 있었다면
                    if ground[i]:
                        # 홈으로 들어오게 된 주자라면
                        if i + active >= 4:
                            cur_point += 1
                        # 진루
                        else:
                            ground[i + active] = 1
                        # 출발한 베이스 초기화
                        ground[i] = 0
            else:
                out_cnt += 1
            # 다음타자 호출
            hitter_index = (hitter_index + 1) % 9
    # 최대 득점인 경우 갱신
    max_point = max(max_point, cur_point)

print(max_point)