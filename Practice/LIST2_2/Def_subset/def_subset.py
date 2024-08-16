# def find_subset(n, arr):=
#     if n == 1:
#         status_arr = list()
#         bit[n - 1] = 0
#         status_arr.append([arr[i] * bit[i] for i in range(elem_number)])
#         bit[n - 1] = 1
#         status_arr.append([arr[i] * bit[i] for i in range(elem_number)])
#
#         return status_arr
#     else:
#         bit[n - 1] = 0
#         find_subset(n - 1, arr)
#         bit[n - 1] = 1
#         find_subset(n - 1, arr)

# n = 3
# union_set = [1, 2, 3]
# elem_number = 3

# print(find_subset(3, union_set))


def find_subset(arr):
    bit = [0]
    status_arr = list()
    bit[0] = 0
    status_arr.append([bit[0] * arr[0]])
    bit[0] = 1
    status_arr.append([bit[0] * arr[0]])

    return status_arr

def find_subset2(n, arr): # n : 부분집합을 구할 집합의 원소의 개수 // arr : 전체집합
    global number, bit, subset_li  # number : 전체집합의 원소의 개수
                                   # bit : 원소의 상태를 나타낸 리스트
                                   # subset_li : 부분집합들을 모아둔 리스트
    if n == 1: # 마지막 원소의 상태 구분단계
        bit[0] = 0
        subset_li.append([bit[i] * arr[i] for i in range(number)])
        bit[0] = 1
        subset_li.append([bit[i] * arr[i] for i in range(number)])

    else: # 첫번째 원소 ~ 마지막 직전까지 구분
        bit[n - 1] = 0
        find_subset2(n - 1, arr)
        bit[n - 1] = 1
        find_subset2(n - 1, arr)

        return subset_li # 할당을 안해 줬기 때문에 맨 처음의 리턴값만 가져오는 것이 가능


# union_set = [1]
# print(find_subset(union_set))

number = 3
union_set2 = [1, 2, 3]
bit = [0] * number
subset_li = list()
print(find_subset2(number, union_set2))

# number = 12
# union_set3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# bit = [0] * 12
# status_arr = list()
# print(find_subset2(number, union_set3))