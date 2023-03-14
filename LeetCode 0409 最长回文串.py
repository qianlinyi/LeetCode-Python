from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        cnt = Counter(s)
        for v in cnt.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
