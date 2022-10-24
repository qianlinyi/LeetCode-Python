class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        mx, mn = [0 for _ in range(n)], [10 ** 6 for _ in range(n)]
        for i in range(n):
            mx[i] = nums[i] if i == 0 else max(nums[i], mx[i - 1])
        for i in range(n - 1, -1, -1):
            mn[i] = nums[i] if i == n - 1 else min(nums[i], mn[i + 1])
        for i in range(n - 1):
            if mx[i] <= mn[i + 1]:
                return i + 1
