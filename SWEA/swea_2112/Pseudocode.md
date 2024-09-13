# 문제 정의
---
## 0. 제약 사항
---
1. **시간제한** :  최대 50개 테스트 케이스를 모두 통과하는데 -> 15초
2. 보호 필름의 **두께 D** -> $3 \leq D \leq 13$
3. 보호 필름의 **가로 W** -> $1 \leq W \leq 20$
4. **합격기준 K** -> $1 \leq W \leq D$
5. 셀이 가질 수 있는 **특성** -> ***A, B*** 두 개만 존재
## 1. 보호 필름을 제작한다.
---
- **필름** :  ***투명한 막을 D***장 세로로 쌓아서 제작
- **막** : 동일한 크기의 ***바 모양의 셀을 가로로 W***개 붙여서 제작
- **셀** : ***특성 A 또는 특성 B***를 가지고 있다.
## 2. 성능 검사
---
- 세로 방향으로 ***동일한 특성의 셀들이 K개 이상 연속적***으로 있는 경우 성능검사를 통과하게 된다.

## 3. 약품
---
- **약품** : 특정 막에 사용하면 해당 막의 모든 셀 특성이 해당 약품의 특성으로 바뀐다.
	- 약품 A -> 모든 셀 특성 A로 변경

## 4. 슈도코드
---
#### 1) 메인
---
``` Pseudocode
# 두께, 가로, 기준
d, w, k <- input

# cell <- 특성 A = 0, 특성 B = 1
film = list(cell_1, cell_2, cell_3, ... cell_d) <- input

count = 0 # 약물 주입 횟수
# 성능검사가 통과 할때까지 약물 주입
if check(film, d, w, k) -> False
	count = injection(film, d, w, k, n, cnt, x)

print(count)
```

#### 2) check 함수
---
``` Pseudocode
def check(film, d, w, k):
	# 필름에서 막 하나씩 가져오기
	for i -> 0 ~ d - 1
		현재 cell XOR 다음 cell
		# k개 만큼 연속한지 체크
	if k개만큼 연속:
		return True
	return False
```

#### 3) injection 함수
---
``` Pseudocode
def injection(film, d, w, k, cnt):
	for i -> d
		if used[i] -> True
			continue
			
		# i번째 위치에 약물 x 투입
		used[i] = True
		for x -> A, B:
			film[i] <- fill x
			# 현재 상태 체크
			status = check(film, d, w, k)
			if status -> True:
				return cnt + 1
			# 다음 막에 약물 x 투입
			injection(film, d, w, k, cnt + 1)
		film[i] <- reset
		used[i] = False
```