class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        suf = [m] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and s[i] == t[j]:
                j -= 1
            suf[i] = j + 1
        ans = suf[0]
        if ans == 0:
            return 0
        j = 0
        for i, c in enumerate(s):
            if c == t[j]:
                j += 1
                ans = min(ans, suf[i + 1] - j)
        return ans
