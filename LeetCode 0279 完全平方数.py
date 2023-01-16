dp = [0, 1] + [10 ** 4] * (10 ** 4)
dp[1] = 1
for i in range(2, 10 ** 4 + 1):
    for j in range(1, 101):
        if j ** 2 > i:
            break
        dp[i] = min(dp[i], 1 + dp[i - j ** 2])


class Solution:
    def numSquares(self, n: int) -> int:
        return dp[n]
