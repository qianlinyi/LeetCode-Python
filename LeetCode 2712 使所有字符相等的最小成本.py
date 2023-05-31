class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        return sum(min(i + 1, n - (i + 1)) for i in range(n - 1) if s[i] != s[i + 1])
