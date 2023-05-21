class UnionSet:
    def __init__(self, n: int):
        self.father = [_ for _ in range(n)]
        self.sz1 = [1 for _ in range(n)]
        self.sz2 = [0 for _ in range(n)]

    def findFather(self, x: int) -> int:
        if self.father[x] == x:
            return x
        self.father[x] = self.findFather(self.father[x])
        return self.father[x]

    def Union(self, x: int, y: int) -> None:
        x, y = self.findFather(x), self.findFather(y)
        self.sz2[y] += 1
        if x == y:
            return
        if self.sz1[x] > self.sz1[y]:
            x, y = y, x
        self.father[x] = y
        self.sz1[y] += self.sz1[x]
        self.sz2[y] += self.sz2[x]


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        u = UnionSet(n)
        for x, y in edges:
            u.Union(x, y)
        s = set()
        ans = 0
        for i in range(n):
            x = u.findFather(i)
            if x not in s:
                s.add(x)
                if (u.sz1[x] - 1) * u.sz1[x] // 2 == u.sz2[x]:
                    ans += 1
        return ans
