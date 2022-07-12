from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        r, c = [0 for _ in range(m)], [0 for _ in range(n)]
        for indice in indices:
            r[indice[0]] += 1
            c[indice[1]] += 1
        oddr, oddc = sum(_ % 2 for _ in r), sum(_ % 2 for _ in c)
        return oddr * (n - oddc) + (m - oddr) * oddc
