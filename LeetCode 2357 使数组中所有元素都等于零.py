class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = add = 0
        for num in nums:
            num -= add
            if num > 0:
                ans += 1
                add += num
        return ans
