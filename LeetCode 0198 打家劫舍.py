from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = cur = 0
        for i in nums:
            cur, pre = max(cur, pre + i), cur
        return cur
