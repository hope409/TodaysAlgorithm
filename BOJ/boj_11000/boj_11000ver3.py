'''
3
1 3
2 4
3 5
'''
### 먼저 시작한 수업이 가장 먼저 끝난다는 걸 고려하지 않았음
### 해당문제를 해결하기 위해 정렬을 한번더 시도해봄
### 시간초과
n = int(input()) # 수업의 개수
classes = [tuple(map(int, input().split())) for _ in range(n)] # 수업 시간표
classes.sort(key=lambda x:x[0]) # 수업 시작시간을 기준으로 정렬
stack = [] # 수업 종료시간을 넣을 스택 생성
cnt = 0 # 현재 사용중인 교실 수를 카운트할 변수
for start, end in classes:
    cnt += 1 # 교실하나 추가로 사용
    if stack: # 진행중인 수업이 있다면?
        # 가장 먼처음에 시작한 수업이 끝나는 시간
        # 현재 수업이 시작하는 시간과 비교해서 더 크다면 교실이 비어있는 거임
        if start >= stack[-1]:
            cnt -= 1
            stack.pop()
    stack.append(end)
    stack.sort(reverse=True)
print(cnt)