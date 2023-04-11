class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rot = dict()
        ans = 0
        cnt1 = cnt2 = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rot[i * n + j] = 0
                    q.append((i, j))
                elif grid[i][j] == 1:
                    cnt1 += 1
        while q and cnt1 != cnt2:
            x0, y0 = q.popleft()
            for x1, y1 in ((x0 + 1, y0), (x0 - 1, y0), (x0, y0 - 1), (x0, y0 + 1)):
                if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == 1:
                    if x1 * n + y1 not in rot:
                        q.append((x1, y1))
                        rot[x1 * n + y1] = rot[x0 * n + y0] + 1
                        ans = max(ans, rot[x1 * n + y1])
                        cnt2 += 1
        if cnt1 == cnt2:
            return ans
        else:
            return -1
