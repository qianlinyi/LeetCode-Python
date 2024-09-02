from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        maxn = max(r for l, r in intervals)
        cnt = [0] * (maxn * 2 + 2)
        # [1,4] [5,6] 不用处理，所以需要放大
        for l, r in intervals:
            cnt[2 * l] += 1
            cnt[2 * r + 1] -= 1
        pre = 0
        ans = []
        s = -1
        for idx, c in enumerate(cnt):
            pre += c
            if pre > 0:
                if s == -1:
                    s = idx
            elif pre == 0:
                if s != -1:
                    ans.append([s // 2, (idx - 1) // 2])
                    s = -1
        return ans
