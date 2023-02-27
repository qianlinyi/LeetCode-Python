class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        return min(
            sum(max(0, nums[i] - min(nums[i + 1] if i - 1 < 0 else nums[i - 1],
                                     nums[i - 1] if i + 1 >= n else nums[i + 1]) + 1)
                for i in range(n) if i % 2 == 0),
            sum(max(0, nums[i] - min(nums[i + 1] if i - 1 < 0 else nums[i - 1],
                                     nums[i - 1] if i + 1 >= n else nums[i + 1]) + 1)
                for i in range(n) if i % 2))
