'''
3
7
13 10 12 11 10 11 12
5
2 4 5 7 9
8
6 6 6 6 6 6 6 6
'''
# 내림, 오름차순으로 정렬하면 가장 높이차이가 낮게 될거라고 생각
# 그러면 양쪽 끝을 연결했을때 해당하는 차이가 가장 큰차이가 되어버림
# 따라서 앞뒤가 연결되어있다고 생각하고 차이를 적게 만드는 방법?
# 좌우에 순서대로 나열하면 차이가 가장 작지 않을까?

t = int(input()) # 테스트케이스 개수
for _ in range(t):
    n = int(input()) # 통나무 개수
    log_list = list(map(int, input().split())) # 통나무의 높이 리스트
    log_list.sort(reverse=True) # 내림차순으로 정리
    left = log_list.pop() # 통나무 배치 시작
    right = log_list.pop()
    level = right - left # 높이차이 계산
    status = False # 왼쪽에 배치할 차례
    while log_list: # 배치할 통나무가 남았다면?
        pre_value = log_list.pop() # 현재 배치해야 할 통나무의 높이
        if log_list: # 마지막 통나무가 아니라면?
            if status: # 오른쪽을 배치할 차례라면?
                level = max(level, pre_value - right) # 높이차이 최대값 계산
                right = pre_value # 오른쪽 갱신
                status = False # 다음은 왼쪽을 배치할 차례 표시
            else: # 왼쪽을 배치할 차례라면?
                level = max(level, pre_value - left) # 높이차이 최대값 계산
                left = pre_value # 왼쪽 갱신
                status = True # 다음은 오른쪽을 배치할 차례 표시
        else: # 마지막 통나무 라면?
            level = max(level, pre_value - right, pre_value - left) # 왼쪽, 오른쪽 둘다 높이차이 계산
    print(level)