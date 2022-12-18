from typing import List


# 二维
class Solution1:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[2000 for _ in range(3)] for _ in range(n)]
        dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2]
        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
        return min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])


# 一维
class Solution2:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        for i in range(1, len(costs)):
            dp = [min(dp[j - 1], dp[j - 2]) + c for j, c in enumerate(costs[i])]
        return min(dp)
