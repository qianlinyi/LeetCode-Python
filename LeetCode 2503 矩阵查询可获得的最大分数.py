import heapq
from heapq import heappop, heappush


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [0] * len(queries)
        q = [(grid[0][0], 0, 0)]
        grid[0][0] = 0
        cnt = 0
        for id, query in sorted(enumerate(queries), key=lambda p: p[1]):
            while q and q[0][0] < query:
                cnt += 1
                _, i, j = heappop(q)
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):  # 枚举周围四个格子
                    if 0 <= x < m and 0 <= y < n and grid[x][y]:
                        heappush(q, (grid[x][y], x, y))
                        grid[x][y] = 0
            ans[id] = cnt
        return ans
