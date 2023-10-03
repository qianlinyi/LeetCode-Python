class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        rg = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in enumerate(edges):
            rg[y].append(x)
            deg[y] += 1

        # 拓扑排序，排序后 deg 值为 1 的点必在基环上，为 0 的点必在树枝上
        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:
            x = q.popleft()
            y = edges[x]
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)

        ans = [0] * n

        # 在反图上遍历树枝
        def rdfs(x, depth):
            ans[x] = depth
            for y in rg[x]:
                if deg[y] == 0:
                    rdfs(y, depth + 1)

        for i, d in enumerate(deg):
            if d <= 0:
                continue
            ring = []
            x = i
            while True:
                deg[x] = -1
                ring.append(x)
                x = edges[x]
                if x == i:
                    break
            for x in ring:
                rdfs(x, len(ring))
        return ans
