class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        while n != 1:
            n //= 2
            temp = nums
            nums = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    nums[i] = min(temp[i << 1], temp[i << 1 | 1])
                else:
                    nums[i] = max(temp[i << 1], temp[i << 1 | 1])
        return nums[0]
