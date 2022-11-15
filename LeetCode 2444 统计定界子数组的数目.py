from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        mn = mx = pos = -1
        for index, num in enumerate(nums):
            if num == minK:
                mn = index
            if num == maxK:
                mx = index
            if not minK <= num <= maxK:
                pos = index
            ans += max(min(mn, mx) - pos, 0)
        return ans
