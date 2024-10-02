# 0. 제약 사항
---
## 1) 아기 상어의 스펙
---
- ### 크기 : 2
- ### 이동 : 상하좌우 1칸씩 이동 가능(1초 소요) / 자신보다 작거나 같은 크기의 물고기가 있는 칸만 이동가능
- ### 먹이 : 자신보다 작은 물고기만 먹을 수 있음 / 자신의 크기와 같은 수의 먹이를 먹으면 크기가 1 커짐
- ### 먹을 수 있는 먹이가 여러개가 있다면?
	- #### 가장 가까운 먹이
	- #### 가장 위에 있는 먹이
	- #### 가장 왼쪽에 있는 먹이
# 1. 문제 해결
---
- 입력을 받을 때 물고기 리스트를 만들자(1차원 리스트)
- 숫자가 더 작은 것이 먹이의 조건에 해당하는 물고기 위치임
- 
# 2. 슈도 코드
---
``` Pseudocode
direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
def move(start, end, length):
	if start == end:
		return length
	else:
		move(start, end, length)

def find(shark_size, shark_position):
	posible_fish_list = sum(fish_list[:shark_size], [])
	next_food = None
	for fish in posible_fish_list:
		pre_food = move(shark_position, fish)
		if next_food is None or pre_food <= next_food:
			if fish < next_size:
				next_food = fish
	return next_food

def main():
	fish_list = [None] * 7
	find(shark_size, shark_position)
```