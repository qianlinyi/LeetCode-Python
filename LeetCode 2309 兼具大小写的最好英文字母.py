from collections import Counter


class Solution:
    def greatestLetter(self, s: str) -> str:
        cnt = Counter(s)
        for i in range(25, -1, -1):
            c = chr(ord('a') + i)
            if cnt[c.upper()] > 0 and cnt[c.lower()] > 0:
                return c.upper()
        return ''
