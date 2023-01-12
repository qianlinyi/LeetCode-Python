class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [10 ** 18] * amount
        for coin in coins:
            for money in range(coin, amount + 1):
                dp[money] = min(dp[money], dp[money - coin] + 1)
        return -1 if dp[-1] == 10 ** 18 else dp[-1]
