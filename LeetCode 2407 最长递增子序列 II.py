from collections import defaultdict
from typing import List


# 线段树，区间更新+最值查询
class Solution:
    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def pushup(self, i: int) -> None:
        self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def pushdown(self, i: int) -> None:
        if self.lazy[i]:
            self.tree[i << 1] = self.tree[i << 1 | 1] = self.lazy[i]
            self.lazy[i << 1] = self.lazy[i << 1 | 1] = self.lazy[i]
            self.lazy[i] = 0

    # 区间更新
    def update(self, i: int, left: int, right: int, start: int, end: int, val: int) -> None:
        if end < left or right < start:
            return
        if start <= left and right <= end:
            self.lazy[i] = self.tree[i] = val
            return
        self.pushdown(i)
        mid = left + right >> 1
        if start <= mid:
            self.update(i << 1, left, mid, start, end, val)
        if end > mid:
            self.update(i << 1 | 1, mid + 1, right, start, end, val)
        self.pushup(i)

    # 区间查询
    def query(self, i: int, left: int, right: int, start: int, end: int) -> int:
        if end < left or right < start:
            return 0
        if start <= left and right <= end:
            return self.tree[i]
        self.pushdown(i)
        mid = left + right >> 1
        ans = 0
        if start <= mid:
            ans = max(ans, self.query(i << 1, left, mid, start, end))
        if end > mid:
            ans = max(ans, self.query(i << 1 | 1, mid + 1, right, start, end))
        return ans

    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        ans = 0
        for num in nums:
            left, right = max(1, num - k), num - 1
            cnt = self.query(1, 1, 100000, left, right)
            ans = max(ans, cnt + 1)
            self.update(1, 1, 100000, num, num, cnt + 1)
        return ans
