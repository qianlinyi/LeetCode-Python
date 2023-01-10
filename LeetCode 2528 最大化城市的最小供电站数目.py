import itertools
from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        pre = list(itertools.accumulate(stations, initial=0))
        for i in range(n):
            stations[i] = pre[min(i + r + 1, n)] - pre[max(i - r, 0)]

        def check(x: int) -> bool:
            diff = [0] * n
            sum, need = 0, 0
            for i, power in enumerate(stations):
                sum += diff[i]
                m = x - power - sum
                if m > 0:
                    need += m
                    if need > k:
                        return False
                    sum += m
                    if i + (r << 1) + 1 < n:
                        diff[i + (r << 1) + 1] -= m
            return True

        left = min(stations)
        right = left + k
        while left <= right:
            mid = left + right >> 1
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
