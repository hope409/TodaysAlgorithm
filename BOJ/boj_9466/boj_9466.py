'''
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
'''

t = int(input()) # 테스트케이스 개수
for _ in range(t):
    n = int(input()) # 학생의 수
    select_number = {i + 1 : int(value) for i, value in enumerate(input().split())} # 선택한 학생의 번호
    non_pair_number = set(range(1, n + 1)) # 최종적으로 짝이 지어지지 않은 학생만 남길 집합
    for first_student in non_pair_number:
        pair_list = set() # 짝지어진 리스트를 담을 리스트
        while True: # 짝 찾기
            pair_list.add(first_student)
            next_student = select_number[first_student]
            if next_student == first_student:
                non_pair_number -= pair_list
                break
            first_student = next_student
    print(len(non_pair_number))

########################################################################################################################

def dfs(student):
    stack = []
    while not visited[student]:  # 방문하지 않은 학생에 대해 순환 탐색
        stack.append(student)
        visited[student] = True
        student = select_number[student]
        if student in stack:  # 순환 발견
            cycle_start = stack.index(student)  # 순환이 시작되는 지점
            in_cycle.update(stack[cycle_start:])  # 순환에 참여하는 학생들 추가
            break
    # 순환을 발견하지 못한 경우 stack은 모두 탐색 완료됨
    for s in stack:
        visited[s] = True

t = int(input())  # 테스트케이스 개수
for _ in range(t):
    n = int(input())  # 학생 수
    select_number = {i + 1: int(value) for i, value in enumerate(input().split())}  # 선택한 학생의 번호

    visited = [False] * (n + 1)  # 방문 여부를 체크하기 위한 리스트
    in_cycle = set()  # 순환에 참여하는 학생을 기록할 집합

    # 모든 학생에 대해 DFS 탐색
    for student in range(1, n + 1):
        if not visited[student]:
            dfs(student)

    # 순환에 참여하지 않은 학생의 수 계산
    result = n - len(in_cycle)
    print(result)

########################################################################################################################

def dfs(student):
    path = []
    while True:
        if cycle_check[student]:  # 이미 순환 확인된 학생인 경우
            for s in path:
                cycle_check[s] = True  # 순환 경로에 포함
            return 0
        if visited[student]:  # 순환이 발견된 경우
            if student in path:  # 순환이 있는 경우만 처리
                cycle_start = path.index(student)  # 순환 시작 인덱스 찾기
                for s in path[cycle_start:]:
                    cycle_check[s] = True  # 순환에 참여하는 학생들 표시
                return len(path[cycle_start:])  # 순환 길이 반환
            else:
                return 0
        # 방문하지 않은 경우 계속 탐색
        path.append(student)
        visited[student] = True
        student = select_number[student]

t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    n = int(input())  # 학생 수
    select_number = {i + 1: int(value) for i, value in enumerate(input().split())}  # 선택한 학생의 번호

    visited = [False] * (n + 1)      # 방문 여부 체크
    cycle_check = [False] * (n + 1)  # 순환 여부 체크

    non_cycle_students = 0
    # 모든 학생에 대해 DFS 탐색
    for student in range(1, n + 1):
        if not visited[student]:
            non_cycle_students += dfs(student)

    # 순환에 포함되지 않은 학생 수 출력
    print(n - non_cycle_students)
