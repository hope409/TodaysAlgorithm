# 0. 제약 사항
---
## 1) 초기상태
---
- 세로, 가로의 크기 : $N, M \rightarrow (1 \leq N \leq 50, 1 \leq M \leq 50)$
- 배양 시간 : $K \rightarrow (1 \leq K \leq 300)$
- 줄기 세포의 생명력 : $X \rightarrow (1 \leq X \leq 10)$
# 1. 문제 해결
---
1) 줄기세포에게 번식된 시간과 유효시간을 같이 입력
2) 만약에 번식하려고 하는데 해당 셀에 줄기세포가 존재한다면?
	1) 번식된 시간을 체크하여 현재 시간과 같으면 덮어쓰기
	2) 같지않으면 패스
3) 배양시간 도달후?
	1) (전체 줄기세포 수) - (죽은 줄기세포 수)
# 2. 슈도 코드
---
``` Pseudocode
def function(k): # k는 배양시간
	for time in range(k):
		update_vessel() # 1시간후
	n = len(grid)
	grid = sum(grid, [])
	result = n ** 2 - grid.count(0) - grid.count(유효시간이 k보다 작은 애들)
```