import itertools


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = list(itertools.accumulate(nums))
        suf = list(itertools.accumulate(nums[::-1]))[::-1]
        n = len(nums)
        if n == 1:
            return 0
        for i in range(n):
            if i == 0:
                if suf[i + 1] == 0:
                    return 0
            elif i == n - 1:
                if pre[i - 1] == 0:
                    return n - 1
            else:
                if pre[i - 1] == suf[i + 1]:
                    return i
        return -1
