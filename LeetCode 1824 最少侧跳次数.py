from cmath import inf


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [1, 0, 1]
        for i in range(1, n):
            mn = inf
            for j in range(3):
                if j == obstacles[i] - 1:
                    dp[j] = inf
                else:
                    mn = min(mn, dp[j])
            for j in range(3):
                if j != obstacles[i] - 1:
                    dp[j] = min(dp[j], mn + 1)
        return min(dp)
