from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n, ans = len(startTime), 0
        for i in range(n):
            if startTime[i] <= queryTime <= endTime[i]:
                ans += 1
        return ans
