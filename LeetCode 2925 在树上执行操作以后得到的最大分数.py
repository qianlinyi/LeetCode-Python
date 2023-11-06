class Solution:

    def maximumScoreAfterOperations(self, edges: List[List[int]],
                                    values: List[int]) -> int:
        g = [[] for _ in range(len(values))]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> int:
            if x != 0 and len(g[x]) == 1:
                return values[x]
            loss = 0
            for y in g[x]:
                if y != fa:
                    loss += dfs(y, x)

            return min(values[x], loss)

        return sum(values) - dfs(0, -1)
