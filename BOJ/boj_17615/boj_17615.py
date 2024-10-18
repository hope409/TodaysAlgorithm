###################################################################
# 빨간색 혹은 파란색 중 하나를 고른다.
# 선택한 공의 색만을 이동시켜서 같은 색 끼리 모은다.
# 최소 횟수를 어떻게 찾을 수 있을까?
# 양쪽 끝에 각각의 색의 공이 몇개씩 있는지?
# 많은쪽으로 해당 공의 색을 이동?
###################################################################
# 좌우에 있는 공의 색을 기준으로 어느방향으로 어떻게 옴길지를 정하려고 했으나
# 생각했던 규칙과 다른 결과가 나와서 모두 고려하는 코드로 선회
###################################################################


n = int(input()) # 공의 개수
ball_list = input() # 공의 리스트
left, right = ball_list[0], ball_list[-1]
blue_ball_list, red_ball_list = ball_list.split('R'), ball_list.split('B') # 해당 색의 공만 분리

# 각각의 방향으로 해당 공을 이동한 횟수
left_blue_move_cnt = 0
left_red_move_cnt = 0
right_red_move_cnt = 0
right_blue_move_cnt = 0

# 왼쪽으로 이동시작
# 빨간공
for ball in red_ball_list[1:]:
    left_red_move_cnt += len(ball)
# 파란공
for ball in blue_ball_list[1:]:
    left_blue_move_cnt += len(ball)
# 오른쪽으로 이동시작
# 빨간공
for ball in red_ball_list[:-1]:
    right_red_move_cnt += len(ball)
# 파란공
for ball in blue_ball_list[:-1]:
    right_blue_move_cnt += len(ball)
# 4개의 값들중 최소값 찾기
print(min(left_blue_move_cnt, left_red_move_cnt, right_red_move_cnt, right_blue_move_cnt))