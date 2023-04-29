import heapq


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append((b, price[b]))
            g[b].append((a, price[a]))

        def dijkstra_path(start, end):  # 存储最短路径
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start, [])]
            while heap:
                d, u, path = heapq.heappop(heap)
                if u == end:
                    return path + [u]
                if d > dist[u]:
                    continue
                for v, w in g[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(heap, (dist[v], v, path + [u]))
            return []

        price_n = [0] * n
        for s, e in trips:
            path = dijkstra_path(s, e)
            for node in path:
                price_n[node] += price[node]
        dp = [[0] * 2 for _ in range(51)]
        for i in range(n):
            dp[i][1] = price_n[i]

        def dfs(x, f):
            for y, _ in g[x]:
                if y != f:
                    dfs(y, x)
                    dp[x][1] += dp[y][0]
                    dp[x][0] += max(dp[y][1], dp[y][0])

        dfs(0, -1)
        return sum(price_n) - max(dp[0][0], dp[0][1]) // 2
