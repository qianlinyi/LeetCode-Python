class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for k, v in cnt.items():
            if v > len(nums) // 2:
                return k
