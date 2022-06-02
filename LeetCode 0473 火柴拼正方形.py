class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks)
        if length % 4:
            return False
        length = length // 4
        dp = [-1] * (1 << len(matchsticks))
        dp[0] = 0
        for s in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if s & (1 << k) == 0:  # 未放入
                    continue
                pre = s & ~(1 << k)
                if dp[pre] >= 0 and dp[pre] + v <= length:
                    dp[s] = (dp[pre] + v) % length
                    break
        return dp[-1] == 0