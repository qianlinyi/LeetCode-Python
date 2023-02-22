import itertools
from collections import Counter
from functools import reduce
from typing import List


def power(a: int, b: int, mod: int) -> int:
    return power(a * a % mod, b >> 1, mod) * (a if b & 1 else 1) % mod if b else 1


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        cnt = Counter(filter(lambda x: all(x % c for c in (4, 9, 25)), nums))
        keys, ans, mod = list(cnt.keys()), 0, 10 ** 9 + 7
        if 1 in keys:
            keys.remove(1)
        for n in range(1, len(keys) + 1):
            for l in itertools.combinations(keys, n):
                prod = reduce(lambda x, y: x * y, l)
                if all(prod % c for c in (4, 9, 25, 49, 121, 169)):
                    ans = (ans + reduce(lambda x, y: x * y % mod, [cnt[_] for _ in l])) % mod
        return ((ans + 1) * (power(2, cnt[1], mod)) - 1) % mod if 1 in cnt else ans
