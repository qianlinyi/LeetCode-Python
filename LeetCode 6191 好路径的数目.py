from collections import defaultdict, Counter
from typing import List


# 并查集
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        father = [_ for _ in range(n)]
        sz = [1 for _ in range(n)]

        def findFather(x: int) -> int:
            if x == father[x]:
                return x
            father[x] = findFather(father[x])
            return father[x]

        def Union(x: int, y: int) -> None:
            x, y = findFather(x), findFather(y)
            if x == y:
                return
            if sz[x] > sz[y]:
                x, y = y, x
            father[x] = y
            sz[y] += sz[x]

        d = defaultdict(list)
        for i in range(n):
            d[vals[i]].append(i)

        g = [[] for _ in range(n)]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        added = [False for _ in range(n)]

        ans = 0
        for _ in sorted(d):
            for i in d[_]:
                added[i] = True
                for j in g[i]:
                    if added[j]:
                        Union(i, j)
            cnt = Counter()
            for i in d[_]:
                cnt[findFather(i)] += 1
            for i in cnt.values():
                ans += i * (i + 1) // 2
        return ans
