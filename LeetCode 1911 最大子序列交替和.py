class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even, odd = nums[0], 0
        for i in range(1, len(nums)):
            even, odd = max(even, odd + nums[i]), max(odd, even - nums[i])
        return even
