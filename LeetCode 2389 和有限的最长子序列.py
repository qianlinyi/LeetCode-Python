import bisect
import itertools


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        suf = list(itertools.accumulate(nums, initial=0))
        ans = []
        for query in queries:
            pos = bisect.bisect_right(suf, query)
            ans.append(pos - 1)
        return ans
