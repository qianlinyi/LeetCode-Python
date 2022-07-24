from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s, ans, dis = start, 0, sum(distance)
        while s != destination:
            ans += distance[s]
            s = (s + 1) % len(distance)
        return min(ans, dis - ans)
