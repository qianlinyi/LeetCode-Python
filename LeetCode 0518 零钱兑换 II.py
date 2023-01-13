class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for money in range(coin, amount + 1):
                dp[money] += dp[money - coin]
        return dp[-1]
