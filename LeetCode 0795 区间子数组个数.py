class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        last2 = last1 = -1
        for i, x in enumerate(nums):
            if left <= x <= right:
                last1 = i
            elif x > right:
                last2 = i
                last1 = -1
            if last1 != -1:
                ans += last1 - last2
        return ans
