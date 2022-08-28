from bisect import bisect_left


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeta(n: int) -> int:
            res = 0
            while n:
                n //= 5
                res += n
            return res

        def nx(k: int) -> int:
            return bisect_left(range(5 * k), k, key=zeta)

        return nx(k + 1) - nx(k)
