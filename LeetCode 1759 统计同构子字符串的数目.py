from itertools import groupby


class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        for k, g in groupby(s):
            n = len(list(g))
            ans += n * (n + 1) // 2
        return ans % (10 ** 9 + 7)
