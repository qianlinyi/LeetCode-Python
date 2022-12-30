class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[10001] * _ for _ in range(1, n)] + [triangle[-1]]
        for i in range(n - 2, -1, -1):
            for j in range(0, i + 1):
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]
