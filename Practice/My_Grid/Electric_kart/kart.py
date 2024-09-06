import sys
sys.stdin = open('sample_input.txt')

# 순열을 만들어 주는 함수
def find_permutation(n): # n : 나열할 사람의 수
    if n == 3:
        size = 6
    elif n == 4:
        size = 24
    elif n == 5:
        size = 120
    elif n == 6:
        size = 720
    elif n == 7:
        size = 5040
    elif n == 8:
        size = 40320
    elif n == 9:
        size = 362880
    permutation_li = [0] * size # 순열 리스트
    idx = 0
    for n1 in range(n): # 첫번째 사람부터 찾아나가기 시작
        for n2 in range(n):
            if n2 == n1:
                continue
            for n3 in range(n):
                if n3 == n2 or n3 == n1: # 이미 나열한 사람이면 패스
                    continue
                if n == 3: # 나열할 사람의 수와 같으면 리스트에 추가
                    permutation_li[idx] = [n1, n2, n3]
                    idx += 1
                    continue
                for n4 in range(n):
                    if n4 == n3 or n4 == n2 or n4 == n1: # 이미 나열한 사람이면 패스
                        continue
                    if n == 4: # 나열할 사람의 수와 같으면 리스트에 추가
                        permutation_li[idx] = [n1, n2, n3, n4]
                        idx += 1
                        continue
                    for n5 in range(n):
                        if n5 == n4 or n5 == n3 or n5 == n2 or n5 == n1: # 이미 나열한 사람이면 패스
                            continue
                        if n == 5: # 나열할 사람의 수와 같으면 리스트에 추가
                            permutation_li[idx] = [n1, n2, n3, n4, n5]
                            idx += 1
                            continue
                        for n6 in range(n):
                            if n6 == n5 or n6 == n4 or n6 == n3 or n6 == n2 or n6 == n1: # 이미 나열한 사람이면 패스
                                continue
                            if n == 6: # 나열할 사람의 수와 같으면 리스트에 추가
                                permutation_li[idx] = [n1, n2, n3, n4, n5, n6]
                                idx += 1
                                continue
                            for n7 in range(n):
                                if n7 == n6 or n7 == n5 or n7 == n4 or n7 == n3 or n7 == n2 or n7 == n1: # 이미 나열한 사람이면 패스
                                    continue
                                if n == 7: # 나열할 사람의 수와 같으면 리스트에 추가
                                    permutation_li[idx] = [n1, n2, n3, n4, n5, n6, n7]
                                    idx += 1
                                    continue
                                for n8 in range(n):
                                    if n8 == n7 or n8 == n6 or n8 == n5 or n8 == n4 or n8 == n3 or n8 == n2 or n8 == n1: # 이미 나열한 사람이면 패스
                                        continue
                                    if n == 8: # 나열할 사람의 수와 같으면 리스트에 추가
                                        permutation_li[idx] = [n1, n2, n3, n4, n5, n6, n7, n8]
                                        idx += 1
                                        continue
                                    for n9 in range(n):
                                        if n9 == n8 or n9 == n7 or n9 == n6 or n9 == n5 or n9 == n4 or n9 == n3 or n9 == n2 or n9 == n1:
                                            continue
                                        if n == 9:
                                            permutation_li[idx] = [n1, n2, n3, n4, n5, n6, n7, n8, n9]
                                            idx += 1
                                            continue
                                        for n10 in range(n):
                                            if n10 == n9 or n10 == n8 or n10 == n7 or n10 == n6 or n10 == n5 or n10 == n4 or n10 == n3 or n10 == n2 or n10 == n1:
                                                continue
                                            if n == 10:
                                                permutation_li[idx] = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
                                                idx += 1
                                                continue
    return permutation_li

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n = int(input()) # 관리구역의 개수
    section_li = [x for x in range(n)]
    energy_li = [list(map(int, input().split())) for _ in range(n)]
    min_energy = None # 에너지의 최소 소모량
    for per_li in find_permutation(n):
        if per_li[0] != 1:
            continue
        pre_energy = 0
        for idx in range(n): # 돌아오는것 까지 확인
            start = per_li[idx] # 시작구역
            end = per_li[(idx + 1) % n] # 도착구역(출발지로 돌아오는거 확인을 위해서 인덱스 계산)
            pre_energy += energy_li[start][end]
        if min_energy is None or pre_energy < min_energy:
            min_energy = pre_energy

    print(f"#{test_case} {min_energy}")

