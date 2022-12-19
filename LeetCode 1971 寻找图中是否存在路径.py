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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        s = UnionSet(n)
        for edge in edges:
            s.Union(edge[0], edge[1])
        return s.findFather(source) == s.findFather(destination)
