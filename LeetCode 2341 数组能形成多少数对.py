from collections import Counter


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans1 = ans2 = 0
        for k, v in cnt.items():
            ans1 += v // 2
            ans2 += v % 2
        return [ans1, ans2]
