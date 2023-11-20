class Solution:

    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        for i in range(n - 1, -1, -1):
            c = 1 << i
            if (c ^ a) * (c ^ b) > a * b:
                a ^= c
                b ^= c
        return a * b % (10**9 + 7)
