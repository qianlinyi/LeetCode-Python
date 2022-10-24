from typing import List


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums_odd, nums_even, target_odd, target_even = [], [], [], []
        for num in nums:
            if num % 2 == 0:
                nums_even.append(num)
            else:
                nums_odd.append(num)
        for num in target:
            if num % 2 == 0:
                target_even.append(num)
            else:
                target_odd.append(num)
        n1, n2 = len(nums_even), len(nums_odd)
        nums_even.sort()
        nums_odd.sort()
        target_even.sort()
        target_odd.sort()
        ans = 0
        for i in range(n1):
            ans += abs(nums_even[i] - target_even[i])
        for i in range(n2):
            ans += abs(nums_odd[i] - target_odd[i])
        return ans // 4
