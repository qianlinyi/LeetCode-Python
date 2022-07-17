from typing import List


# 循环节
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            cnt = 0
            while nums[i] < n:
                num = nums[i]
                nums[i] = n
                i = num
                cnt += 1
            ans = max(ans, cnt)
        return ans
