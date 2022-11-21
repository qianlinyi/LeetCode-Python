from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        g = [[] for _ in range(n)]
        ans = 0
        for road in roads:
            g[road[0]].append(road[1])
            g[road[1]].append(road[0])

        def dfs(cur: int, fa: int) -> (int, int):
            nonlocal ans
            car, people = 0, 0
            for nxt in g[cur]:
                if nxt != fa:
                    x, y = dfs(nxt, cur)
                    car, people = car + x, people + y
            ans += car
            people += 1
            return (people + seats - 1) // seats, people

        dfs(0, -1)
        return ans
