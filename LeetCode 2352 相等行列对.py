class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res, n = 0, len(grid)
        cnt = Counter(tuple(row) for row in grid)
        res = 0
        for col in zip(*grid):
            res += cnt[tuple(col)]
        return res
