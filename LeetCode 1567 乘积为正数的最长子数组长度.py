class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        positive, negative = [1 if nums[0] > 0 else 0] + [0] * (n - 1), [1 if nums[0] < 0 else 0] + [0] * (n - 1)
        ans = positive[0]
        for i in range(1, n):
            if nums[i] > 0:
                positive[i] = positive[i - 1] + 1
                negative[i] = negative[i - 1] + 1 if negative[i - 1] else 0
            elif nums[i] < 0:
                positive[i] = negative[i - 1] + 1 if negative[i - 1] else 0
                negative[i] = positive[i - 1] + 1
            else:
                positive[i] = 0
                negative[i] = 0
            ans = max(ans, positive[i])
        return ans
