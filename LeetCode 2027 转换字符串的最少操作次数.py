class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = idx = 0
        while idx < len(s):
            if s[idx] == 'X':
                idx += 3
                ans += 1
            else:
                idx += 1
        return ans
