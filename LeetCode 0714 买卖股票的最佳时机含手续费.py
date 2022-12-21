# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         # dp[i][0] 手持股票的最大收益
#         # dp[i][1] 不持股票的最大收益
#         n = len(prices)
#         dp = [[-prices[0], 0]] + [[0] * 2 for _ in range(n - 1)]
#         for i in range(1, n):
#             dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
#             dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - fee + prices[i])
#         return dp[-1][1]

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(sell, buy - fee + prices[i]), max(buy, sell - prices[i])
        return sell
