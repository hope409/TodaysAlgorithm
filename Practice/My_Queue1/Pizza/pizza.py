# import sys
# sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n, m = map(int, input().split()) # n : 화덕의 용량 / m : 피자의 수
    pizza = list(map(int, input().split())) # 치즈의 양
    fire_pit = [0] * n # 현재 화덕 상태
    front, rear = -1, 0# 초기 설정
    cnt = 0
    while True:
        if fire_pit[rear] == 0:
            if front < m - 1:  # 피자가 남았다면?
                front += 1 # 다음순번의 피자
                fire_pit[rear] = [front, pizza[front]] # 해당 번호와 피자를 화덕에 투입
                rear = (rear + 1) % n
                cnt += 1
            else:
                rear = (rear + 1) % n
        else:
            fire_pit[rear][1] //= 2 # 피자의 치즈가 줄어듬
            if fire_pit[rear][1] == 0: # 줄어든 후 치즈가 다 녹았을 때
                if front < m - 1: # 피자가 남았다면?
                    front += 1
                    fire_pit[rear] = [front, pizza[front]] # 해당 번호와 피자를 화덕에 투입
                else:
                    fire_pit[rear] = [-1, -1]
                    cnt -= 1
                    if cnt == 1:
                        break
            rear = (rear + 1) % n
    for i in range(n):
        if fire_pit[i][1] != -1:
            print(f"#{test_case} {fire_pit[i][0] + 1}")
            break