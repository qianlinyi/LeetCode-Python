import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10 ** 9 + 7
        l = min(a, b)
        r = n * min(a, b)
        c = math.lcm(a, b)
        while l <= r:
            mid = l + r >> 1
            cnt = mid // a + mid // b - mid // c
            if cnt >= n:
                r = mid - 1
            else:
                l = mid + 1
        return (r + 1) % mod
