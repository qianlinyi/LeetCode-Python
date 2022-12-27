from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[] for _ in range(numRows)]
        dp[0] = [1]
        for i in range(1, numRows):
            dp[i].append(1)
            for j in range(0, len(dp[i - 1]) - 1):
                dp[i].append(dp[i - 1][j] + dp[i - 1][j + 1])
            dp[i].append(1)
        return dp
