class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] + [0] * rowIndex
        for i in range(1, rowIndex + 1):
            ans[i] = ans[i - 1] * (rowIndex - i + 1) // i
        return ans
