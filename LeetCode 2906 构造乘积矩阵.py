class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]

        suf = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = suf
                suf = suf * grid[i][j] % MOD

        pre = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = p[i][j] * pre % MOD
                pre = pre * grid[i][j] % MOD
        return p
