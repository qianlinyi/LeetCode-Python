class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        mx = nums[0]
        for num in nums:
            if mx >= num:
                ans += mx - num
                mx = mx + 1
            else:
                mx = num + 1
        return ans
