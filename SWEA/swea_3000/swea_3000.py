'''
1
3 5
1 3
2 6
8 9
'''
import heapq

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1):
    n, start_num = map(int, input().split()) # 주어질 숫자쌍 초기값
    result = 0
    num_li = [start_num]
    garbage_li = []
    for i in range(1, n + 1):
        num1, num2 = map(int, input().split()) # 주어진 숫자쌍
        heapq.heappush(num_li, num1)
        heapq.heappush(num_li, num2)
        cur_left = heapq.heappop(num_li)
        heapq.heappush(garbage_li, -cur_left) # 버릴 숫자
        if num_li[0] < -garbage_li[0]:
            temp1 = heapq.heappop(num_li)
            temp2 = heapq.heappop(garbage_li)
            heapq.heappush(garbage_li, -temp1)
            heapq.heappush(num_li, -temp2)
        result += num_li[0]
        result %= 20171109
    print(f'#{test_case} {result}')