def make_permutation(n, k, permutation): # n : 원소의 개수, k : 현재 나열한 원소의 수, permutation : 현재 만들고있는 순열
    if n == k:
        return
    for i in range(n):
        if used[i]:
            continue
        permutation.append(i)
        used[i] = True
        make_permutation(n, k + 1, permutation)
        permutation.pop()
        used[i] = False

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 관리구역의 개수
    energy_li = [list(map(int, input().split())) for _ in range(n)] # 에너지 소모량
    permutations = [] # 순열들을 넣을 리스트
    used = [False] * n
    make_permutation(n, 0, [])
    min_energy = None # 에너지의 최소 소모량
    for per_li in permutations:
        if per_li[0] != 0:
            continue
        pre_energy = 0
        for idx in range(n):  # 돌아오는것 까지 확인
            start = per_li[idx]  # 시작구역
            end = per_li[(idx + 1) % n]  # 도착구역(출발지로 돌아오는거 확인을 위해서 인덱스 계산)
            pre_energy += energy_li[start][end]
        if min_energy is None or pre_energy < min_energy:
            min_energy = pre_energy
    print(f"#{test_case} {min_energy}")