class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mxSum, mnSum = 0, 0
        mxAns, mnAns = -3 * 10 ** 4, 3 * 10 ** 4
        for num in nums:
            mxSum = max(num, mxSum + num)
            mxAns = max(mxAns, mxSum)
            mnSum = min(num, mnSum + num)
            mnAns = min(mnAns, mnSum)
        s = sum(nums)
        return max(mxAns, s - mnAns) if mxAns > 0 else mxAns
