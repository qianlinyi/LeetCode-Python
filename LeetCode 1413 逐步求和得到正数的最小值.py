from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum, ans = 0, 1
        for num in nums:
            sum += num
            if 1 - sum > 0:
                ans = max(ans, 1 - sum)
        return ans
