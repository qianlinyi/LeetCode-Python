from functools import reduce


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = reduce(lambda x, y: x * y, nums)
        if result > 0:
            return 1
        elif result < 0:
            return -1
        else:
            return 0
