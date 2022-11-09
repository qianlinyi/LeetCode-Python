class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1 for _ in range(n)] for _ in range(n)]
        for mine in mines:
            grid[mine[0]][mine[1]] = 0
        u, d, l, r = [[0 for _ in range(n)] for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)], [
            [0 for _ in range(n)] for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if j == 0:
                    l[i][j] = (1 if grid[i][j] == 1 else 0)
                    u[j][i] = (1 if grid[j][i] == 1 else 0)
                else:
                    l[i][j] = (0 if grid[i][j] == 0 else 1 + l[i][j - 1])
                    u[j][i] = (0 if grid[j][i] == 0 else 1 + u[j - 1][i])
            for j in reversed(range(n)):
                if j == n - 1:
                    r[i][j] = (1 if grid[i][j] == 1 else 0)
                    d[j][i] = (1 if grid[j][i] == 1 else 0)
                else:
                    r[i][j] = (0 if grid[i][j] == 0 else 1 + r[i][j + 1])
                    d[j][i] = (0 if grid[j][i] == 0 else 1 + d[j + 1][i])
        ans = 0
        for i in range(n):
            for j in range(n):
                ans = max(ans, min(u[i][j], d[i][j], l[i][j], r[i][j]))
        return ans
