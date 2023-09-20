class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = max(nums)
        for i in range(n):
            res = 0
            for j in count(1):
                idx = (i + 1) * j * j - 1
                if idx >= n: break
                res += nums[idx]
            ans = max(ans, res)
        return ans
