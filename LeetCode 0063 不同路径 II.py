class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j - 1]
                    elif j == 0:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
