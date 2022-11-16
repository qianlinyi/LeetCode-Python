# 区间求和+区间更新成同一值
class SegTree:
    def __init__(self, n: int):
        self.tree = [0] * (n << 2)
        self.lazy = [0] * (n << 2)

    def pushup(self, i: int) -> None:
        self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def pushdown(self, i: int, left: int, right: int) -> None:
        if self.lazy[i]:
            mid = left + right >> 1
            self.tree[i << 1] = self.lazy[i] * (mid - left + 1)
            self.tree[i << 1 | 1] = self.lazy[i] * (right - mid)
            self.lazy[i << 1] = self.lazy[i << 1 | 1] = self.lazy[i]
            self.lazy[i] = 0

    def build(self, i: int, left: int, right: int):
        if left == right:
            self.tree[i] = 0
            return
        mid = left + right >> 1
        self.build(i << 1, left, mid)
        self.build(i << 1 | 1, mid + 1, right)
        self.pushup(i)

    # 区间更新
    def update(self, i: int, left: int, right: int, start: int, end: int, val: int) -> None:
        if end < left or right < start:
            return
        if start <= left and right <= end:
            self.lazy[i] = val
            self.tree[i] = val * (right - left + 1)
            return
        self.pushdown(i, left, right)
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
        self.pushdown(i, left, right)
        mid = left + right >> 1
        ans = 0
        if start <= mid:
            ans += self.query(i << 1, left, mid, start, end)
        if end > mid:
            ans += self.query(i << 1 | 1, mid + 1, right, start, end)
        return ans


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # 线段树超时
        # tree, n, g, l = SegTree(100001), len(nums), 0, 0
        # for i in reversed(range(n)):
        #     val = tree.query(1, 1, 100001, 1, nums[i])
        #     tree.update(1, 1, 100001, nums[i] + 1, nums[i] + 1, val + 1)
        #     g += val
        #     if i > 0 and nums[i] < nums[i - 1]:
        #         l += 1
        # return g == l
        return all(abs(x - i) <= 1 for i, x in enumerate(nums))
