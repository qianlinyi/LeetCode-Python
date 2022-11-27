class Solution:
    def check(self, nums: List[int]) -> bool:
        return any(sorted(nums) == nums[i:] + nums[:i] for i in range(len(nums)))
