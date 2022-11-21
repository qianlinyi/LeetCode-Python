class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.] * 100 for _ in range(101)]

        for i in range(query_row + 1):
            for j in range(query_glass + 1):
                if i == 0 and j == 0:
                    dp[i][j] = poured
                elif i == 0:
                    dp[i][j] = 0.
                elif j == 0:
                    dp[i][j] = max(0., (dp[i - 1][j] - 1) / 2)
                else:
                    dp[i][j] = max(0., (dp[i - 1][j - 1] - 1) / 2) + max(0., (dp[i - 1][j] - 1) / 2)
        return min(1., dp[query_row][query_glass])
