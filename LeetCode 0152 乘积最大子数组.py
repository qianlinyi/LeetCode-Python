class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mnSum = mxSum = 1
        ans = -10 ** 18
        for num in nums:
            mn, mx = mnSum, mxSum
            mxSum = max(num * mx, num * mn, num)
            mnSum = min(num * mn, num * mx, num)
            ans = max(ans, mxSum)
        return ans
