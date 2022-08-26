from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx1 = mx2 = 0
        for num in nums:
            if num >= mx1:
                mx2 = mx1
                mx1 = num
            elif mx1 > num > mx2:
                mx2 = num
        return (mx1 - 1) * (mx2 - 1)
