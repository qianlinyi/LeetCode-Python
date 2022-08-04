from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans, nums = [], sorted(nums)[::-1]
        for i in range(1, len(nums) + 1):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
