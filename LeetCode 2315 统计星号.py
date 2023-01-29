class Solution:
    def countAsterisks(self, s: str) -> int:
        s = '|' + s + '|'
        ans = 0
        id = 0
        for c in s:
            if c == '|':
                id += 1
            else:
                if id & 1 and c == '*':
                    ans += 1
        return ans
