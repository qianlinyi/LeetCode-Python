class MyCalendarTwo:
    def __init__(self):
        self.tree = {}

    def update(self, start: int, end: int, val: int, left: int, right: int, idx: int) -> None:
        if right < start or end < left:
            return
        if start <= left and right <= end:
            p = self.tree.get(idx, [0, 0])
            p[0] += val
            p[1] += val
            self.tree[idx] = p
            return
        mid = (left + right) // 2
        self.update(start, end, val, left, mid, 2 * idx)
        self.update(start, end, val, mid + 1, right, 2 * idx + 1)
        p = self.tree.get(idx, [0, 0])
        p[0] = p[1] + max(self.tree.get(2 * idx, (0,))[0], self.tree.get(2 * idx + 1, (0,))[0])
        self.tree[idx] = p

    def book(self, start: int, end: int) -> bool:
        self.update(start, end - 1, 1, 0, 10 ** 9, 1)
        if self.tree[1][0] > 2:
            self.update(start, end - 1, -1, 0, 10 ** 9, 1)
            return False
        return True
