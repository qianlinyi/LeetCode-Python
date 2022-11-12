from cmath import inf


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0 for _ in range(4)] for _ in range(n + 1)]
        dp[0][3] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][3]
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][3] = sum(dp[i - 1][_] for _ in range(4)) % MOD
        return dp[n][3]
