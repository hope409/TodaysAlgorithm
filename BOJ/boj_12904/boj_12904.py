#################################
# A는 무조건 뒤에다가 추가
# B는 뒤집고 뒤에다가 추가
### 그러면 B는 맨처음엔 앞에 그다음엔 뒤에 붙인다고 생각해보자
# 그러다가 해당 모양이 나오는지 확인
from collections import deque
init_str = list(input())
trans_str = [str(x) for x in input()]

while trans_str:
    if len(trans_str) < len(init_str):
        print(0)
        break
    elif init_str == trans_str:
        print(1)
        break
    elif trans_str[-1] == 'A':
        trans_str.pop()
    elif trans_str[-1] == 'B':
        trans_str.pop()
        trans_str.reverse()
else:
    print(0)