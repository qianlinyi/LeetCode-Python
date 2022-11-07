from cmath import inf
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort(key=lambda x: x[0])
        robot.sort()
        m = len(robot)
        f = [0] + [inf] * m
        for pos, limit in factory:
            for j in range(m, 0, -1):
                cost = 0
                for k in range(1, min(j, limit) + 1):
                    cost += abs(robot[j - k] - pos)
                    f[j] = min(f[j], f[j - k] + cost)
        return f[m]
