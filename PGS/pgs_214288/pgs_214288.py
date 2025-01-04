import heapq
from itertools import product

def solution(k, n, reqs): # k : 상담유형의 개수 / n : 멘토의 수 / reqs : [a 분에, b분 길이의 상담, c번 유형의 상담]
    delay = None
    # 가능한 멘토의 수 조합
    remain_mento_li = [list(mento_li) for mento_li in product(range(1, n - k + 2), repeat=k) if sum(mento_li) == n]
    for mento_li in remain_mento_li:
        pre_delay = 0
        mento_schedule = [[] for _ in range(k)]
        for req in reqs:
            # 이미 최소값을 넘어 버렸다면?
            if delay is not None and pre_delay > delay:
                break

            a, b, c = req
            # 최초의 스케줄이라면?
            if not mento_schedule[c - 1]:
                heapq.heappush(mento_schedule[c - 1], a + b)
                mento_li[c - 1] -= 1
            # 최초의 스케줄이 아니라면?
            else:
                # 상담시작 시간이 가장 최근 상담 종료시간 보다 크면?
                if a >= mento_schedule[c - 1][0]:
                    heapq.heappop(mento_schedule[c - 1])
                    heapq.heappush(mento_schedule[c - 1], a + b)
                # 그렇지 않은데 멘토가 아직 남아있다면?
                elif mento_li[c - 1]:
                    heapq.heappush(mento_schedule[c - 1], a + b)
                    mento_li[c - 1] -= 1
                # 멘토가 남아있지 않다면?
                else:
                    end = heapq.heappop(mento_schedule[c - 1])
                    pre_delay += end - a
                    heapq.heappush(mento_schedule[c - 1], end + b)

        # 최소값이라면 갱신
        if delay is None or pre_delay < delay:
            delay = pre_delay

    return delay