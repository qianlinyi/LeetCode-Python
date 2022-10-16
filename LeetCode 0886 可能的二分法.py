from typing import List


# DFS
# class Solution:
#     def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
#         g = [[] for _ in range(n)]
#         for x, y in dislikes:
#             g[x - 1].append(y - 1)
#             g[y - 1].append(x - 1)
#         color = [0] * n
#
#         def dfs(x: int, c: int) -> bool:
#             color[x] = c
#             return all(color[y] != c and (color[y] or dfs(y, -c)) for y in g[x])
#
#         return all(c or dfs(i, 1) for i, c in enumerate(color))


# 并查集
class UnionSet:
    def __init__(self, n: int):
        self.father = [_ for _ in range(n)]
        self.sz = [1 for _ in range(n)]

    def findFather(self, x: int) -> int:
        if self.father[x] == x:
            return x
        self.father[x] = self.findFather(self.father[x])
        return self.father[x]

    def Union(self, x: int, y: int) -> None:
        x, y = self.findFather(x), self.findFather(y)
        if x == y:
            return
        if self.sz[x] > self.sz[y]:
            x, y = y, x
        self.father[x] = y
        self.sz[y] += self.sz[x]


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        u = UnionSet(n)
        for x, nodes in enumerate(g):
            for y in nodes:
                u.Union(nodes[0], y)
                if u.findFather(x) == u.findFather(y):
                    return False
        return True
