from functools import cache


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10 ** 9 + 7

        def f(s: str) -> int:
            @cache
            def f(i: int, sum: int, is_limit: bool) -> int:
                if sum > max_sum:
                    return 0
                if i == len(s):
                    return int(sum >= min_sum)
                res = 0
                up = int(s[i]) if is_limit else 9
                for d in range(up + 1):
                    res += f(i + 1, sum + d, is_limit and d == up)
                return res % MOD

            return f(0, 0, True)

        ans = f(num2) - f(num1) + (min_sum <= sum(map(int, num1)) <= max_sum)
        return ans % MOD