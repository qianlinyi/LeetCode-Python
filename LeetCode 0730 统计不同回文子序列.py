# DP
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod, n = 10 ** 9 + 7, len(s)
        dp = [[[0] * n for _ in range(n)] for _ in range(4)]
        for i, c in enumerate(s):
            dp[ord(c) - ord('a')][i][i] = 1
        for t in range(2, n + 1):
            for j in range(t - 1, n):  # 注意i和j的变化，i和j的间距由小变大
                i = j - t + 1
                for k, c in enumerate('abcd'):
                    if s[i] == c and s[j] == c:
                        dp[k][i][j] = (2 + sum(d[i + 1][j - 1] for d in dp)) % mod
                    elif s[i] == c:
                        dp[k][i][j] = dp[k][i][j - 1]
                    elif s[j] == c:
                        dp[k][i][j] = dp[k][i + 1][j]
                    else:
                        dp[k][i][j] = dp[k][i + 1][j - 1]
        return sum(d[0][n - 1] for d in dp) % mod
