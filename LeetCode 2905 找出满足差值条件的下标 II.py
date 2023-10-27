class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        mx = mn = 0
        for j in range(indexDifference, len(nums)):
            i = j - indexDifference
            if nums[i] > nums[mx]:
                mx = i
            elif nums[i] < nums[mn]:
                mn = i
            if nums[mx] - nums[j] >= valueDifference:
                return [mx, j]
            if nums[j] - nums[mn] >= valueDifference:
                return [mn, j]
        return [-1, -1]
