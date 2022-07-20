from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        ans = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                ans[(i + (j + k) // c) % r][(j + k) % c] = grid[i][j]
        return ans
