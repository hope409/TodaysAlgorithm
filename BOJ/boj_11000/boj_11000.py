'''
3
1 3
2 4
3 5
'''

# 메모리 초과
# schedule을 카운트배열로 만들어서 전부다 세어 보려고 했음
# 처음 시도해 보기 전까지도 메모리초과가 날것 같았음
# 혹시나 해서 해보았는데 역시나 안됌

n = int(input()) # 수업의 개수
class_list = [0] * n # 수업시간표 리스트
max_end = 0 # 가장 늦게 끝나는 수업시간
for i in range(n):
    start, end = map(int, input().split()) # 수업 시작, 끝
    class_list[i] = (start, end) # 수업시간표에 추가
    max_end = max(max_end, end) # 가장 늦게 끝나는 수업 찾기
schedule = [0] * max_end # 가장 늦게 끝나는 수업을 기준으로 카운트배열 생성
for start, end in class_list: # 카운트하기
    for j in range(start, end):
        schedule[j] += 1 # 해당하는 시간표에 필요한 교실의 갯수 추가
print(max(schedule))