# 直接遍历
from bisect import bisect_left

from sortedcontainers import SortedDict


class MyCalendar1:

    def __init__(self):
        self.d = {}

    def book(self, start: int, end: int) -> bool:
        flag = True
        for key, value in self.d.items():
            if end <= key or start >= value:
                continue
            else:
                flag = False
                break
        if flag:
            self.d[start] = end
        return flag


# 二分
class MyCalendar2:

    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> bool:
        index = self.d.bisect_left(end)
        if index == 0 or self.d.items()[index - 1][1] <= start:
            self.d[start] = end
            return True
        else:
            return False


# 线段树
class MyCalendar3:

    def __init__(self):
        self.tree = set()
        self.lazy = set()

    def update(self, start: int, end: int, l: int, r: int, i: int) -> None:
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree.add(i)
            self.lazy.add(i)
        else:
            mid = l + r >> 1
            self.update(start, end, l, mid, i << 1)
            self.update(start, end, mid + 1, r, i << 1 | 1)
            self.tree.add(i)
            if i << 1 in self.lazy and i << 1 | 1 in self.lazy:
                self.lazy.add(i)

    def query(self, start: int, end: int, l: int, r: int, i: int) -> bool:
        if r < start or end < l:
            return False
        if i in self.lazy:
            return True
        if start <= l and r <= end:
            return i in self.tree
        mid = l + r >> 1
        return self.query(start, end, l, mid, i << 1) or self.query(start, end, mid + 1, r, i << 1 | 1)

    def book(self, start: int, end: int) -> bool:
        if self.query(start, end - 1, 0, 10 ** 9, 1):
            return False
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return True
