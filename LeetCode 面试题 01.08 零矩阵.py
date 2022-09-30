from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = len(matrix), len(matrix[0])
        row, col = [True for _ in range(r)], [True for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row[i] = col[j] = False
        for i in range(r):
            for j in range(c):
                if row[i] == False or col[j] == False:
                    matrix[i][j] = 0
        return matrix
