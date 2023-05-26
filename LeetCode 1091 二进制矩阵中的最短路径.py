from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        vis = dict()
        step = [0] * (n * n + 1)
        step[0] = 1
        vis[0] = 1
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            if x == y == n - 1:
                return step[x * n + y]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    xx, yy = x + i, y + j
                    if xx * n + yy in vis or xx < 0 or xx >= n or yy < 0 or yy >= n or grid[xx][yy] == 1:
                        continue
                    step[xx * n + yy] = step[x * n + y] + 1
                    vis[xx * n + yy] = 1
                    q.append((xx, yy))
        return -1
