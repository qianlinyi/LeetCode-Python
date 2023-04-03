from collections import deque


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def bfs(s: int) -> int:
            d = [-1] * n
            d[s] = 0
            q = deque([(s, -1)])
            while q:
                x, fa = q.popleft()
                for y in g[x]:
                    if d[y] == -1:
                        d[y] = d[x] + 1
                        q.append((y, x))
                    elif y != fa:
                        return d[x] + d[y] + 1
            return inf

        ans = min(bfs(i) for i in range(n))
        return ans if ans < inf else -1
