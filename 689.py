def maxSumOfThreeSubarrays(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    window_sum = [sum(nums[:k])]
    for i in range(1, n - k + 1):
        window_sum.append(window_sum[-1] - nums[i - 1] + nums[i + k - 1])

    left = [0] * len(window_sum)
    right = [0] * len(window_sum)

    max_idx = 0
    for i in range(len(window_sum)):
        if window_sum[i] > window_sum[max_idx]:
            max_idx = i
        left[i] = max_idx

    max_idx = len(window_sum) - 1
    for i in range(len(window_sum) - 1, -1, -1):
        if window_sum[i] >= window_sum[max_idx]:
            max_idx = i
        right[i] = max_idx

    max_sum = 0
    ans = [-1, -1, -1]

    for j in range(k, len(window_sum) - k):
        l, r = left[j - k], right[j + k]
        current_sum = window_sum[l] + window_sum[j] + window_sum[r]
        if current_sum > max_sum:
            max_sum = current_sum
            ans = [l, j, r]
        elif current_sum == max_sum:
            ans = min(ans, [l, j, r])

    return ans

# Ví dụ
nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
print(maxSumOfThreeSubarrays(nums, k))  # Output: [0, 3, 5]
