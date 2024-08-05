class Solution:

    def quickSelect(self, nums, l, r, k):
        if l == r:
            return nums[k]
        partition = nums[l]
        i, j = l - 1, r + 1
        while i < j:
            flag = True
            while flag:
                i += 1
                if nums[i] >= partition:
                    flag = False
            flag = True
            while flag:
                j -= 1
                if nums[j] <= partition:
                    flag = False
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        if k <= j:
            return self.quickSelect(nums, l, j, k)
        else:
            return self.quickSelect(nums, j + 1, r, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return self.quickSelect(nums, 0, n - 1, n - k)
