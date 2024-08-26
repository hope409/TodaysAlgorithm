'''
2
4 0 0 0 0 0 0 0 0
4 0 0 0 0 0 0 0 0
'''
n = int(input()) # 이닝의 수
hitter_li = [list(map(int, input().split())) for _ in range(n)] # 타자들의 각 이닝별 행동
pre_num = 0 # 현재 출전할 타자 번호(인덱스번호)
pas_num = 0 # 마지막으로 홈에 들어온 타자 번호(인덱스번호)
score = 0 # 현재 점수
for hit in hitter_li: # 첫번째 이닝부터 시작
    pas_num = pre_num # 첫번째 타자 설정
    out_cnt = 0 # 아웃카운트 리셋
    base_li = [0] * 9 # 각 타자 번호별 현재 위치 / 0: 홈, 1: 1루, 2: 2루, 3: 3루
    while out_cnt != 3: # 아웃카운트가 3이되면 해당 이닝 종료
        if hit[pre_num] == 0: # 아웃카운트 하나 증가 후 다음타자
            out_cnt += 1
            pre_num = (pre_num + 1) % 9  # 아웃될 때까지 계속 순환
            continue
        elif hit[pre_num] == 4: # 홈런을 쳤을때
            score += 10 - base_li.count(0)
            base_li = [0] * 9 # 베이스 리셋
            pre_num = (pre_num + 1) % 9  # 아웃될 때까지 계속 순환
            pas_num = pre_num
            continue
        base_li[pre_num] += hit[pre_num] # 타자 베이스로 이동
        idx = pas_num # 가장 앞에 있는 주자 번호
        while idx != pre_num: # 주자들 전체
            if base_li[idx] == 0: # 아웃된 타자라면
                pas_num = (pas_num + 1) % 9 # 다음 주자 탐색
                continue

            base_li[idx] += hit[pre_num] # 해당 베이스만큼 이동
            if base_li[idx] >= 4: # 홈에 들어왔다면?
                base_li[idx] = 0 # 홈으로 복귀
                score += 1
                pas_num = (pas_num + 1) % 9
            idx = (idx + 1) % 9
        pre_num = (pre_num + 1) % 9 # 아웃될 때까지 계속 순환

print(score) # 점수 출력