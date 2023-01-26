class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ''
        while k:
            c = min(26, k - (n - 1))
            ans = chr(ord('a') + c - 1) + ans
            k = k - c
            n -= 1
        return ans
