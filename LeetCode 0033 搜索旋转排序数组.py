class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + r >> 1
            a, b, c = nums[l], nums[mid], nums[r]
            if a == target:
                return l
            if b == target:
                return mid
            if c == target:
                return r
            if a < b:
                if a < target < b:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if b < target < c:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
