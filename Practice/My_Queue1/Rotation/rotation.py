import sys
sys.stdin = open('sample_input.txt')

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n, m = map(int, input().split()) # n : 숫자 개수 / m : 회전 횟수
    num_arr = list(map(int, input().split())) # 숫자 배열 받아오기

    front, rear = 0, -1 # 초기 설정
    for _ in range(m): # 회전 시작
        front = (front + 1) % n
        rear = (rear + 1) % n
    print(f"#{test_case} {num_arr[front]}")