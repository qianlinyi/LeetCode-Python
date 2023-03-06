from collections import deque
from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        g = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        s = {(x, y) for x, y in guesses}
        ans = cnt0 = 0

        def dfs(x: int, father: int) -> None:
            nonlocal cnt0
            for y in g[x]:
                if y != father:
                    cnt0 += (x, y) in s
                    dfs(y, x)

        dfs(0, -1)

        def reroot(x: int, father: int, cnt: int) -> None:
            nonlocal ans
            ans += cnt >= k
            for y in g[x]:
                if y != father:
                    reroot(y, x, cnt - ((x, y) in s) + ((y, x) in s))

        reroot(0, -1, cnt0)
        return ans

