'''
8
0 1 0 1 0 0 0 1
2
1 3
2 3
'''

n = int(input()) # 스위치 수
led_li = list(map(int, input().split())) # 스위치 상태
st_num = int(input()) # 학생 수
gender_li = []
idx_li = []
for _ in range(st_num):
    gender, idx = map(int, input().split())
    gender_li.append(gender)
    idx_li.append(idx)
for i in range(st_num):
    gender = gender_li[i]
    idx = idx_li[i]
    cnt1 = idx # 남학생 계산시 쓸 카운트
    cnt2 = 0 # 여학생 계산시 쓸 카운트
    if gender == 1: # 남학생 일때
        while idx <= n:
            if led_li[idx - 1] == 1:
                led_li[idx - 1] = 0
            else:
                led_li[idx - 1] = 1
            idx += cnt1
    else: # 여학생 일때
        while 0 <= idx - 1 + cnt2 < n and 0 <= idx - 1 - cnt2 < n and led_li[idx - 1 + cnt2] == led_li[idx - 1 - cnt2]:
            if led_li[idx - 1 + cnt2] == 1:
                led_li[idx - 1 + cnt2] = 0
                led_li[idx - 1 - cnt2] = 0
            else:
                led_li[idx - 1 + cnt2] = 1
                led_li[idx - 1 - cnt2] = 1
            cnt2 += 1
for i in range(1, 1 + n): # 출력
    if i % 10 == 0:
        print(led_li[i - 1])
    else:
        print(led_li[i - 1], end=' ')
