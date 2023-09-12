import cmath
import itertools


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        f, t = [], []
        for i, row in enumerate(grid):
            for j, cnt in enumerate(row):
                if cnt > 1:
                    f.extend([(i, j)] * (cnt - 1))
                elif cnt == 0:
                    t.append((i, j))
        ans = cmath.inf
        for f2 in itertools.permutations(f):
            total = 0
            for (x1, y1), (x2, y2) in zip(f2, t):
                total += abs(x1 - x2) + abs(y1 - y2)
            ans = min(ans, total)
        return ans
