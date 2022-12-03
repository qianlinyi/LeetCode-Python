class Solution:
    def secondHighest(self, s: str) -> int:
        mx = ans = -1
        for c in s:
            if c.isdigit():
                if ord(c) - ord('0') > mx:
                    ans = mx
                    mx = ord(c) - ord('0')
                elif ord(c) - ord('0') != mx and ord(c) - ord('0') > ans:
                    ans = ord(c) - ord('0')
        return ans
