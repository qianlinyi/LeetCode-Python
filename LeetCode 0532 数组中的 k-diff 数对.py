from typing import List


# 哈希表
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        vis, ans = set(), set()
        for num in nums:
            if num - k in vis:
                ans.add(num - k)
            if num + k in vis:
                ans.add(num)
            vis.add(num)
        return len(ans)
