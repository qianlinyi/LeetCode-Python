from collections import defaultdict


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        mask = defaultdict(int)
        for i, nums in enumerate((nums1, nums2, nums3)):
            for num in nums:
                mask[num] |= 1 << i
        return [k for k, v in mask.items() if v & (v - 1)]
