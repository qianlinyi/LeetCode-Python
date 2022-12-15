class Solution:
    def getLucky(self, s: str, k: int) -> int:
        p, s = s, ''
        for c in p:
            s += str(ord(c) - ord('a') + 1)
        while k:
            sum = 0
            for c in s:
                sum += int(c)
            s = str(sum)
            k -= 1
        return int(s)
