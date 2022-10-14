class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10 ** 9 + 7

        g = [0] * 26
        total = 0
        for i, ch in enumerate(s):
            oi = ord(s[i]) - ord("a")
            g[oi], total = (total + 1) % mod, (total * 2 + 1 - g[oi]) % mod

        return total
