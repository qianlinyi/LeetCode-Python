class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ans = 1
        for coin in coins:
            if coin > ans:
                break
            ans += coin
        return ans
