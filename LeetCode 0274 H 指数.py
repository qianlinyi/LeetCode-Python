import bisect


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        l, r = 1, n
        while l <= r:
            mid = l + r >> 1
            pos = bisect.bisect_left(citations, mid)
            if n - pos >= mid:
                l = mid + 1
            else:
                r = mid - 1
        return r
