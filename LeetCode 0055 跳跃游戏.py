class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        mx = 0
        for i in range(0, n):
            if mx >= i:
                mx = max(mx, i + nums[i])
        return mx >= n - 1
