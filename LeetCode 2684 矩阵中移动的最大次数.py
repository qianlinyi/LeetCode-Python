from functools import cache


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(x, y, pre):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] <= pre:
                return -1
            return max(dfs(x - 1, y + 1, grid[x][y]), dfs(x, y + 1, grid[x][y]), dfs(x + 1, y + 1, grid[x][y])) + 1

        return max(dfs(i, 0, 0) for i in range(m))
