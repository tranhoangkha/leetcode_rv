import functools

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        @functools.cache
        def de(i=0, total=0):
            print(f"Calling de(i={i}, total={total})")  # In ra giá trị của i và total
            if i == len(nums):
                print(f"Reached end: i={i}, total={total}, total == target: {total == target}")
                return total == target
            add = de(i + 1, total + nums[i])
            sub = de(i + 1, total - nums[i])
            print(f"At i={i}, total={total}, add={add}, sub={sub}")  # In kết quả add, sub
            return add + sub
        
        return de()

# Ví dụ
nums = [1, 1, 1, 1, 1]
target = 3

solution = Solution()
result = solution.findTargetSumWays(nums, target)
print(f"Result: {result}")  # In kết quả cuối cùng
