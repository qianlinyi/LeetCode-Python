from random import randrange
from typing import List


# 哈希表
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        m = len(blacklist)
        self.bound = w = n - m
        black = {b for b in blacklist if b >= self.bound}
        self.b2w = {}
        for b in blacklist:
            if b < self.bound:
                while w in black:
                    w += 1
                self.b2w[b] = w
                w += 1

    def pick(self) -> int:
        x = randrange(self.bound)
        return self.b2w.get(x, x)
