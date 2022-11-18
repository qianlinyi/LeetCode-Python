from typing import List


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        mod = 10 ** 9 + 7
        x, y = nums[0], 2
        for j in range(1, len(nums)):
            res = (res + nums[j] * (y - 1) - x) % mod
            x = (x * 2 + nums[j]) % mod
            y = y * 2 % mod
        return res % mod
