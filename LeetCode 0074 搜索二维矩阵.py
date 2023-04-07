import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        num = [row[-1] for row in matrix]
        pos1 = bisect.bisect_left(num, target)
        if pos1 == m:
            return False
        pos2 = bisect.bisect_left(matrix[pos1], target)
        return matrix[pos1][pos2] == target
