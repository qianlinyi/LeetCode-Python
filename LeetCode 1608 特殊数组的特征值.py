from bisect import bisect_left
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums) + 1):
            pos = bisect_left(nums, i)
            if len(nums) - pos == i:
                return i
        return -1
