'''
4 4
3 0 1 4
'''
h, w = map(int, input().split())
blocks = list(map(int, input().split()))
sum_water = 0
# 일층부터 확인해 나가기
for floor in range(h):
    # 현재층 담긴 물의 양
    pre_water = 0
    # 왼쪽에 벽으로 둘러쌓여있는가?
    status = False
    for block in blocks:
        # 현재층에 벽이 있는가?
        block -= floor
        # 벽의 개수가 음수가 되었다면 0으로 초기화
        if block < 0:
            block = 0
        # 벽이 있다면 지금까지 쌓인 물을 합치기
        if block:
            status = True
            sum_water += pre_water
            pre_water = 0
        # 왼쪽에 벽이 있다면 물 한칸 추가
        elif status:
            pre_water += 1
print(sum_water)