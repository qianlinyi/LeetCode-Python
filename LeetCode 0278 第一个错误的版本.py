# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r, ans = 1, n, 0
        while l <= r:
            mid = l + r >> 1
            if isBadVersion(mid)==False:
                l = mid + 1
            else:
                r = mid - 1
        return l