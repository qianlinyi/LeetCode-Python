from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans, r, c = [], len(mat), len(mat[0])
        for i in range(r + c - 1):
            if i % 2:
                x = 0 if i < c else i - c + 1
                y = i if i < c else c - 1
                while x < r and y >= 0:
                    ans.append(mat[x][y])
                    x, y = x + 1, y - 1
            else:
                x = i if i < r else r - 1
                y = 0 if i < r else i - r + 1
                while x >= 0 and y < c:
                    ans.append(mat[x][y])
                    x, y = x - 1, y + 1
        return ans
