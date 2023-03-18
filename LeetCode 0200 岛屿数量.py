class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= m or y < 0 or y >= n or (x * n + y in vis) or grid[x][y] == '0':
                return
            vis[x * n + y] = 1
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        vis = dict()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and i * n + j not in vis:
                    dfs(i, j)
                    ans += 1
        return ans
