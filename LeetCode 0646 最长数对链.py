from cmath import inf
from typing import List


# 排序 + 贪心
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, ans = -inf, 0
        for x, y in sorted(pairs, key=lambda p: p[1]):
            if cur < x:
                cur = y
                ans += 1
        return ans
