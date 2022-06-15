from bisect import bisect_left
from typing import List


# 二分 + 双指针
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(mid: int) -> int:
            cnt, left = 0, 0
            for right, num in enumerate(nums):
                while num - nums[left] > mid:
                    left += 1
                cnt += right - left
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)
