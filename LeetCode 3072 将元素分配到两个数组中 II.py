# 线段树区间更新, 区间求和
class Tree:
    def __init__(self, n: int):
        self.tree = [0] * (n << 2)
        self.lazy = [0] * (n << 2)

    def pushup(self, i: int) -> None:
        self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def pushdown(self, i: int, left: int, right: int) -> None:
        if self.lazy[i]:
            mid = left + right >> 1
            self.lazy[i << 1] += self.lazy[i]
            self.lazy[i << 1 | 1] += self.lazy[i]
            self.tree[i << 1] += (mid - left + 1) * self.lazy[i]
            self.tree[i << 1 | 1] += (right - mid) * self.lazy[i]
            self.lazy[i] = 0

    # 区间更新
    def update(self, i: int, left: int, right: int, start: int, end: int, val: int) -> None:
        if end < left or right < start:
            return
        if start <= left and right <= end:
            self.lazy[i] += val
            self.tree[i] += (right - left + 1) * val
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
    def resultArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        index = dict()
        for i, num in enumerate(sorted_nums):
            index[num] = i
        m = len(sorted_nums)
        t1 = Tree(m)
        t2 = Tree(m)
        arr1, arr2 = [nums[0]], [nums[1]]
        t1.update(1, 1, m, index[nums[0]], index[nums[0]], 1)
        t2.update(1, 1, m, index[nums[1]], index[nums[1]], 1)
        for i in range(2, len(nums)):
            cnt1 = t1.query(1, 1, m, index[nums[i]] + 1, m)
            cnt2 = t2.query(1, 1, m, index[nums[i]] + 1, m)
            if cnt1 > cnt2:
                t1.update(1, 1, m, index[nums[i]], index[nums[i]], 1)
                arr1.append(nums[i])
            elif cnt2 > cnt1:
                t2.update(1, 1, m, index[nums[i]], index[nums[i]], 1)
                arr2.append(nums[i])
            else:
                len1 = len(arr1)
                len2 = len(arr2)
                if len1 > len2:
                    t2.update(1, 1, m, index[nums[i]], index[nums[i]], 1)
                    arr2.append(nums[i])
                else:
                    t1.update(1, 1, m, index[nums[i]], index[nums[i]], 1)
                    arr1.append(nums[i])
        return arr1 + arr2
