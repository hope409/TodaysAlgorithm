'''
9 3
1 2 3 4 5 6 7 8 9
'''


def min_max_partition(nums, k):
    n = len(nums)
    target = sum(nums) // k
    min_max = float('inf')

    def backtrack(index, sums):
        nonlocal min_max
        if index == n:
            max_sum = max(sums)
            min_max = min(min_max, max_sum)
            return

        for i in range(k):
            sums[i] += nums[index]
            if sums[i] <= target:  # 현재 집합의 합이 목표를 초과하지 않도록
                backtrack(index + 1, sums)
            sums[i] -= nums[index]

            # 현재 집합이 비어있다면, 더 이상의 집합을 채우지 않도록
            if sums[i] == 0:
                break

    sums = [0] * k
    backtrack(0, sums)

    return min_max

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = min_max_partition(nums, m)
print(result)
