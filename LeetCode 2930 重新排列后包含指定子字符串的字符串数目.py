class Solution:

    def stringCount(self, n: int) -> int:
        MOD = 10**9 + 7
        NoL = 25**n
        NoT = 25**n
        AtMostOneE = 25**n + n * 25**(n - 1)
        NoLAndNoT = 24**n
        NoLAndAtMostOneE = 24**n + n * 24**(n - 1)
        NoTAndAtMostOneE = 24**n + n * 24**(n - 1)
        NoLAndNoTAndAtMostOneE = 23**n + n * 23**(n - 1)
        return (26**n -
                (NoL + NoT + AtMostOneE - NoLAndNoT - NoLAndAtMostOneE -
                 NoTAndAtMostOneE + NoLAndNoTAndAtMostOneE)) % MOD
