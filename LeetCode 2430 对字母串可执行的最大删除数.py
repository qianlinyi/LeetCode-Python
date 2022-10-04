# DP
class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        lcp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] != s[j]:
                    lcp[i][j] = 0
                else:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
        dp = [0 for _ in range(n + 1)]
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            for j in range(1, (n - i >> 1) + 1):
                if lcp[i][i + j] >= j:
                    dp[i] = max(dp[i], dp[i + j] + 1)
        return dp[0]
