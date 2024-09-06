import sys
sys.stdin = open('sample_input.txt')

def find_min_energy(n, k, current_energy, start): # n : 구역의 개수 / k : 살펴본 구역의 개수 / current_energy : 현재 사용 에너지 / start : 출발지
    global min_energy
    if k == n:
        current_energy += energy_li[start][0]  # 마지막 구역에서 출발지로 돌아오는 에너지
        if min_energy is None or current_energy < min_energy:
            min_energy = current_energy
        return

    for next in range(1, n):
        if used[next]:
            continue
        next_energy = current_energy + energy_li[start][next]
        if min_energy is not None and next_energy >= min_energy:
            continue  # 이미 최소 에너지보다 크다면 탐색 중단
        used[next] = True
        find_min_energy(n, k + 1, next_energy, next)
        used[next] = False

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    energy_li = [list(map(int, input().split())) for _ in range(n)]
    min_energy = None
    used = [False] * n
    find_min_energy(n, 1, 0, 0)  # 출발지는 0으로 고정
    print(f"#{test_case} {min_energy}")
