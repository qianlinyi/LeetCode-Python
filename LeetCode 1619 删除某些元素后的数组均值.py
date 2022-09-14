from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        d = len(arr) // 20
        ans = 0
        arr.sort()
        for num in arr[d:len(arr) - d]:
            ans += num
        return ans / (len(arr) - 2 * d)
