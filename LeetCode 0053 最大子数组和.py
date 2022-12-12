# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         ans, n = nums[0], len(nums)
#         dp = [nums[0]] + [0] * (n - 1)
#         for i in range(1, n):
#             dp[i] = max(nums[i], nums[i] + dp[i - 1])
#             ans = max(ans, dp[i])
#         return ans

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10 ** 4
        sum = 0
        for num in nums:
            sum = max(sum + num, num)
            ans = max(ans, sum)
        return ans
