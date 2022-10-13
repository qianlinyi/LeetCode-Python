from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans, sum = 0, 0
        for i, num in enumerate(arr):
            sum += num
            if sum == i * (i + 1) // 2:
                ans += 1
        return ans
