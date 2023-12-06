import bisect


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for pos, num in enumerate(numbers):
            res = target - num
            if res < num:
                continue
            p = bisect.bisect_left(numbers, res, lo=pos + 1)
            if p == len(numbers):
                continue
            if numbers[p] == res:
                return [pos + 1, p + 1]
