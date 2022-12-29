class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[101] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][max(0, j - 1)], dp[i - 1][min(n - 1, j + 1)])
        return min(dp[n - 1])
