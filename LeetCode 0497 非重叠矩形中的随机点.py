# 前缀和 + 二分
from bisect import bisect_right
from random import randrange
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.sum = [0]
        for a, b, x, y in rects:
            self.sum.append(self.sum[-1] + (x - a + 1) * (y - b + 1))  # 二维转一维，前缀和存取

    def pick(self) -> List[int]:
        k = randrange(self.sum[-1])
        index = bisect_right(self.sum, k) - 1  # 二分查找
        a, b, x, y = self.rects[index]
        div, mod = divmod(k - self.sum[index], x - a + 1)  # 一维转二维
        return [a + mod, b + div]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
