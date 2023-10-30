class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp1 = dp2 = dp3 = 0
        for num in nums:
            dp1, dp2, dp3 = min(dp1, dp2, dp3) + max(0, k - num), dp1, dp2
        return min(dp1, dp2, dp3)
