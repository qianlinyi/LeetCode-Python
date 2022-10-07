from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        i, n = 0, len(nums)
        while i < n:
            s = nums[i]
            i += 1
            while i < n and nums[i] > nums[i - 1]:
                s += nums[i]
                i += 1
            ans = max(ans, s)
        return ans
