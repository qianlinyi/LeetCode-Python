class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        res = abs(sum(nums) - goal)
        return (res + limit - 1) // limit
