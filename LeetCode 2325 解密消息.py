class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = dict()
        ch = ord('a')
        for c in key:
            if c.isalpha() and c not in d:
                d[c] = chr(ch)
                ch += 1
        ans = ''
        for c in message:
            if c.isalpha():
                ans += d[c]
            else:
                ans += c
        return ans
