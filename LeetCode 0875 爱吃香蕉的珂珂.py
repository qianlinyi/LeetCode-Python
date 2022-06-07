class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def judge(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours <= h

        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if judge(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
