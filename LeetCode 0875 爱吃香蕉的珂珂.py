from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def judge(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours <= h

        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if judge(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
