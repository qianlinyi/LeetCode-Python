from collections import deque


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        d = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图
            d[x] += 1
            d[y] += 1

        q = deque()
        for i, (deg, c) in enumerate(zip(d, coins)):
            if deg == 1 and c == 0:
                q.append(i)
        while q:
            for y in g[q.popleft()]:
                d[y] -= 1
                if d[y] == 1 and coins[y] == 0:
                    q.append(y)

        for i, (deg, c) in enumerate(zip(d, coins)):
            if deg == 1 and c:
                q.append(i)
        if len(q) <= 1:
            return 0
        t = [0] * n
        while q:
            x = q.popleft()
            for y in g[x]:
                d[y] -= 1
                if d[y] == 1:
                    t[y] = t[x] + 1
                    q.append(y)
        return sum(t[x] >= 2 and t[y] >= 2 for x, y in edges) * 2
