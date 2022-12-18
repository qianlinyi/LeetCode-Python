class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, mn = 0, prices[0]
        for price in prices:
            ans = max(ans, price - mn)
            mn = min(mn, price)
        return ans
