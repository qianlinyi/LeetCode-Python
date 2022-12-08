from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mx = max(nums)
        cnt = Counter(nums)
        cur = pre = 0
        for i in range(mx + 1):
            cur, pre = max(cur, pre + i * cnt[i]), cur
        return cur
