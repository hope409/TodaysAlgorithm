'''
1
0
'''

########################################################
# 문제의 핵심 2, 1성장 물뿌리개를 동시에 사용해야 한다.
# 따라서 나무의 높이들은 그 합이 3의 배수여야 한다.
# 3의 배수라고 다 되는 것도 아니고 2와 1의 조합이 들어맞아야 한다.
# 위의 조건 두개를 큰 두가지 분기점으로 두고 문제 해결 시작
########################################################


n = int(input()) # 사과나무 개수
apple_trees = list(map(int, input().split())) # 원하는 사과나무의 높이
sum_height = sum(apple_trees)
# 나무 크기의 합이 3의 배수가 아니라면? 불가능
if sum_height % 3:
    print('NO')

else:
    # 물뿌리개를 몇번 사용해야 하는지 계산
    cnt_two = sum_height // 3
    # 2짜리 물뿌리개의 남은 사용횟수 재할당
    remain_cnt = cnt_two
    for i in range(n):
        # 현재 나무에 뿌릴수 있는 2짜리 물뿌리개의 횟수
        pre_cnt = apple_trees[i] // 2
        # 만약 남은 횟수를 다 사용해도 불가능한 높이면?
        if remain_cnt <= pre_cnt:
            # 가능한 만큼만 물뿌리개 사용
            pre_cnt = pre_cnt - remain_cnt
            apple_trees[i] = apple_trees[i] - 2 * remain_cnt
            # 남은 횟수 0으로 만들기
            remain_cnt = 0
            break
        # 가능한 만큼 물뿌리개 사용
        remain_cnt -= pre_cnt
        # 나무 성장 시키기
        apple_trees[i] = apple_trees[i] % 2
    # 남은 사과나무의 높이의 합이 곧 1짜리 물뿌리개 사용횟수
    # 이때 그 횟수가 2짜리 물뿌리개 사용횟수와 같다면 키울 수 있다.
    if cnt_two == sum(apple_trees):
        print('YES')
    else:
        print('NO')