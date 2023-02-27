import heapq
from cmath import inf
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] - grid[0][0] > 1 and grid[1][0] - grid[0][0] > 1:
            return -1
        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = 0
        q = [(0, 0, 0)]
        while q:
            d, x, y = heapq.heappop(q)
            if x == m - 1 and y == n - 1:
                return d
            for tx, ty in (x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y):
                if 0 <= tx < m and 0 <= ty < n:
                    nd = max(d + 1, grid[tx][ty])
                    nd += (nd - tx - ty) % 2
                    if nd < dis[tx][ty]:
                        dis[tx][ty] = nd
                        heapq.heappush(q, (nd, tx, ty))