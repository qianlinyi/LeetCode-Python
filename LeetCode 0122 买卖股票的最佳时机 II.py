class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(0, len(prices) - 1):
            ans += max(prices[i + 1] - prices[i], 0)
        return ans
