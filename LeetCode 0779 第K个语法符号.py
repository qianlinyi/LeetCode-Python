class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k -= 1
        ans = 0
        while k:
            k &= k - 1
            ans ^= 1
        return ans
