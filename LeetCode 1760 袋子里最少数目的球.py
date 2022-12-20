class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            mid = l + r >> 1
            if sum((num + mid - 1) // mid - 1 for num in nums) <= maxOperations:
                r = mid - 1
            else:
                l = mid + 1
        return l
