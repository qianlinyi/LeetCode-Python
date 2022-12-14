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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda e: e[2])
        ans, k = [False] * len(queries), 0
        s = UnionSet(n)
        for i, (p, q, limit) in sorted(enumerate(queries), key=lambda p: p[1][2]):
            while k < len(edgeList) and edgeList[k][2] < limit:
                s.Union(edgeList[k][0], edgeList[k][1])
                k += 1
            ans[i] = s.findFather(p) == s.findFather(q)
        return ans
