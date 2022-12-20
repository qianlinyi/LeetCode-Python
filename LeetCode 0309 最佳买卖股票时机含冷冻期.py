class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        # dp[i][0] 手持股票的最大收益
        # dp[i][1] 手上不持股票，且处于冷冻期的最大收益
        # dp[i][2] 手上不持股票，且不处于冷冻期的最大收益
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[-1][1], dp[-1][2])
