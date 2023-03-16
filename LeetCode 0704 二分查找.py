class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l if l < len(nums) and nums[l] == target else -1
