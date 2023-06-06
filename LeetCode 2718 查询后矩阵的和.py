from collections import defaultdict


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_take = set()
        col_take = set()
        ans = 0
        for t, index, val in queries[::-1]:
            if t == 0:
                if index in row_take:
                    continue
                row_take.add(index)
                ans += (n - len(col_take)) * val
            else:
                if index in col_take:
                    continue
                col_take.add(index)
                ans += (n - len(row_take)) * val
        return ans
