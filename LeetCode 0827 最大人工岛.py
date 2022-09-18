from collections import Counter
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tag = [[0 for _ in range(n)] for _ in range(n)]
        area = Counter()

        def dfs(i: int, j: int) -> None:
            tag[i][j] = t
            area[t] += 1
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < n and 0 <= y < n and grid[x][y] and tag[x][y] == 0:
                    dfs(x, y)

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v and tag[i][j] == 0:
                    t = i * n + j + 1
                    dfs(i, j)
        ans = max(area.values(), default=0)

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 0:
                    new_area = 1
                    connected = {0}
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                        if 0 <= x < n and 0 <= y < n and tag[x][y] not in connected:
                            new_area += area[tag[x][y]]
                            connected.add(tag[x][y])
                    ans = max(ans, new_area)
        return ans
