class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

        def get(x: int, y: int) -> int:
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return dp[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + k + 1, j + k + 1) - get(i - k, j + k + 1) - get(i + k + 1, j - k) + get(i - k,
                                                                                                            j - k)
        return ans
