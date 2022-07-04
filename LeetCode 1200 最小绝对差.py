from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans, mindif = [], 2 * 10 ** 6
        for i in range(len(arr) - 1):
            mindif = min(mindif, arr[i + 1] - arr[i])
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == mindif:
                ans.append([arr[i], arr[i + 1]])
        return ans
