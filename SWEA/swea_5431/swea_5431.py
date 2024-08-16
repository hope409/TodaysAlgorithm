'''

# SWEA 5431번

# 문제 해석
> 1. 학생 수와 과제를 제출한 번호가 몇번인지 알려준다.
> 2. 이때 과제를 제출하지 않은 사람을 빈칸을 두고 출력해준다.

# 발상
> 1. 전체 학생 리스트를 하나 만들고 과제 제출 학생 리스트도 하나 만들어준다.
> 2. 이때 인덱스 번호 = 학생 번호 - 1 이다.
> 3. 따라서 과제 제출 학생의 원소 - 1 위치의 값을 빼주면 해당 학생의 원소를 지울 수 있다.
> 4. 한번 지우고 난 다음에는 한칸씩 땡겨지기 때문에 몇명의 원소를 지웠는지 추가로 빼준다.

'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    st_n, sub_n = map(int, input().split())
    st_li = list(map(lambda x : x + 1, range(st_n)))
    sub_li = list(map(int, input().split()))
    sub_li.sort()
    n = 0
    for i in sub_li:
        st_li.pop(i-1-n)
        n = n + 1
    for i in range(len(st_li)):
        if i == 0:
            print(f"#{test_case}", end=' ')
        print(st_li[i],end = ' ')
    print()