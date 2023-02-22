from typing import List


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        cnt1 = [0] * (4 * n)
        flip = [False] * (4 * n)

        def pushup(i: int) -> None:
            cnt1[i] = cnt1[i << 1] + cnt1[i << 1 | 1]

        def pushdown(i: int, l: int, r: int) -> None:
            cnt1[i] = r - l + 1 - cnt1[i]
            flip[i] = not flip[i]

        def build(i: int, l: int, r: int) -> None:
            if l == r:
                cnt1[i] = nums1[l - 1]
                return
            mid = l + r >> 1
            build(i << 1, l, mid)
            build(i << 1 | 1, mid + 1, r)
            pushup(i)

        def update(i: int, l: int, r: int, start: int, end: int) -> None:
            if start <= l and r <= end:
                pushdown(i, l, r)
                return
            mid = l + r >> 1
            if flip[i]:
                pushdown(i << 1, l, mid)
                pushdown(i << 1 | 1, mid + 1, r)
                flip[i] = False
            if mid >= start:
                update(i << 1, l, mid, start, end)
            if mid < end:
                update(i << 1 | 1, mid + 1, r, start, end)
            pushup(i)

        build(1, 1, n)
        ans, s = [], sum(nums2)
        for op, l, r in queries:
            if op == 1:
                update(1, 1, n, l + 1, r + 1)
            elif op == 2:
                s += l * cnt1[1]
            else:
                ans.append(s)
        return ans
