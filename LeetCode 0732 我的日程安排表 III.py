from collections import defaultdict


class MyCalendarThree:

    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def pushup(self, i: int):
        self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def pushdown(self, i: int):
        if self.lazy[i]:
            self.lazy[i << 1] += self.lazy[i]
            self.lazy[i << 1 | 1] += self.lazy[i]
            self.tree[i << 1] += self.lazy[i]
            self.tree[i << 1 | 1] += self.lazy[i]
            self.lazy[i] = 0

    def update(self, start: int, end: int, left: int, right: int, i: int):
        if right < start or end < left:
            return
        if start <= left and right <= end:
            self.tree[i] += 1
            self.lazy[i] += 1
        else:
            self.pushdown(i)
            mid = (left + right) // 2
            self.update(start, end, left, mid, i << 1)
            self.update(start, end, mid + 1, right, i << 1 | 1)
            self.pushup(i)

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return self.tree[1]

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
