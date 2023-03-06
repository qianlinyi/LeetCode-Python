class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        ans, cnta, cntb = n, [0] * n, [0] * n
        for i in range(n):
            cntb[i] = (s[i] == 'b') + (cntb[i - 1] if i > 0 else 0)
        for i in range(n - 1, -1, -1):
            cnta[i] = (s[i] == 'a') + (cnta[i + 1] if i < n - 1 else 0)
        for i in range(-1, n):
            ans = min(ans, (cnta[i + 1] if i < n - 1 else 0) + (cntb[i] if i > 0 else 0))
        return ans
