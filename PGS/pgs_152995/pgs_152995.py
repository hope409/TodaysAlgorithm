# 고려를 안한 부분
# 1. 나보다 종합 점수가 높지만 인센티브 대상이 아닐 수가 있다.
# 반례 [[100, 10], [85, 60], [70, 65], [80, 70]]

def solution2(scores):
    answer = 1
    my_score = scores[0]
    my_sum = sum(my_score)
    for score in scores:
        # 만약 두 평가 점수 모두 내 점수 이상이라면?
        if score[0] > my_score[0] and score[1] > my_score[1]:
            answer = -1
            break
        # 둘다 높진 않지만 합이 나보다 높다면?
        if sum(score) > my_sum:
            answer += 1

    return answer

# 첫 번째 문제에 대해서 고려사항을 추가
# 1. 우선 앞선 코드에서 고려했던 부분은 당연히 고려 해야함
# 2. 단지 추가로 종합 점수가 높지만 인센티브 대상이 아닌 대상은 내 앞의 순위에서 제거해야함
# 3. 따라서 지금 보고있는 대상의 점수가 다른 사원이랑 비교했을 때 인센티브 대상이 아닌지를 판단해야함
# 4. 근무 태도 점수로 내림차순을 정렬하고 순서대로 비교를 한다면?
# 5. 즉 0번째 인덱스의 사원이 아닌 이상 근무 태도 점수는 낮다는 것
# 6. 이때 동료 태도 점수를 어떻게 비교해야 할까?
# 7. 지금까지 나온 동료 태도 점수들 중에서 가장 높은사원이랑 비교 했을 때 그거보다 작으면 둘다 작은 사원 아닐까?
# 8. 그럼 이걸 효율적으로 비교하는 방법이 뭘까?
# 9. 고려해야 할 대상에 대해서 다시 정리해보자
# 9-1. 지금까지 나온 동료 태도 점수의 최대값 보다 작은 대상들을 찾아야 한다.
# 9-2. 그러면 두가지 케이스를 모두 내림차순 정렬해서 비교하면 되지 않을까?
# 10. 그리고 인센티브 제외 대상을 고려하는 과정에 본인도 확인을 하기 때문에 아래에서는 재차 확인하는 과정을 생략한다.

def solution3(scores):
    answer = 1
    my_score = scores[0]
    my_sum = sum(my_score)
    max_corp_score = 0

    scores.sort(key = lambda x: (-x[0], -x[1]))

    for score in scores:
        if score[1] < max_corp_score:
            if score == my_score:
                answer = -1
                break
            continue
        else:
            max_corp_score = score[1]

        if sum(score) > my_sum:
            answer += 1

    return answer

# 또 다시 문제가 발생
# 논리상으로는 맞는데 프로그램 로직상 문제가 있는 것 같다.
# 동료 평가 점수를 내림차순하면 발생하는 문제
# scores = [[10, 3], [10, 2], [10, 1], [9, 4], [9, 3], [9, 2], [9, 1]]
# 위와같은 케이스의 경우 두번째 점수인 동료 평가 점수를 내림차순하면 발생하는 문제가 있는데
# 해당 케이스에서는 [9, 3]의 점수를 받은 사원은 인센티브 제외 대상이 아니다.
# 하지만 내가 짠 코드에서 로직상 해당 사원은 [9, 4] 케이스에서 동료 평가 점수의 최대값이 4로 갱신된 후
# 비교를 진행하기 때문에 인센티브 제외 대상 취급을 받아버린다. 즉 근무 태도 점수가 같다는 걸 고려하지 못하는 문제가 발생한다.
# 따라서 동료 평가 점수를 낮은 순으로 비교하는 것으로 해당 문제를 해결한다. 즉 오름차순 정렬 후 진행

def solution(scores):
    answer = 1
    my_score = scores[0]
    my_sum = sum(my_score)
    max_corp_score = 0

    scores.sort(key = lambda x: (-x[0], x[1]))

    for score in scores:
        if score[1] < max_corp_score:
            if score == my_score:
                answer = -1
                break
            continue

        else:
            max_corp_score = score[1]

        if sum(score) > my_sum:
            answer += 1

    return answer