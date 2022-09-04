from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        row, col = [0 for _ in range(r)], [0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if mat[i][j]:
                    row[i] += 1
                    col[j] += 1
        ans = 0
        for i in range(r):
            for j in range(c):
                if row[i] + col[j] == 2 and mat[i][j]:
                    ans += 1
        return ans
