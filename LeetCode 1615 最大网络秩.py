class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d, ans, connect = [0] * n, 0, [[False] * n for _ in range(n)]
        for i, j in roads:
            d[i] += 1
            d[j] += 1
            connect[i][j] = 1
            connect[j][i] = 1
        for i in range(n):
            for j in range(n):
                ans = max(ans, d[i] + d[j] - connect[i][j])
        return ans
