from typing import List
from queue import PriorityQueue


# DP + 优先队列
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        ans, fuel, prev, h = 0, startFuel, 0, PriorityQueue()
        for i in range(n + 1):
            cur = stations[i][0] if i < n else target
            fuel -= cur - prev
            while fuel < 0 and h.qsize():
                fuel -= h.get()
                ans += 1
            if fuel < 0:
                return -1
            if i < n:
                h.put(-stations[i][1])
                prev = cur
        return ans
