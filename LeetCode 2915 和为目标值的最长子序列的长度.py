class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [0] + [-inf] * target
        s = 0
        for x in nums:
            s = min(s + x, target)
            for j in range(s, x - 1, -1):
                dp[j] = max(dp[j], dp[j - x] + 1)
        return dp[-1] if dp[-1] > 0 else -1
