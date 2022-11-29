class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        dp = [[0, 1]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            if s[i] == s[i - 1]:
                dp[i][1] = dp[i - 1][0] + 1
                dp[i][0] = dp[i - 1][1]
            else:
                dp[i][1] = dp[i - 1][1] + 1
                dp[i][0] = dp[i - 1][0]
        return min(dp[n - 1][0], dp[n - 1][1])
