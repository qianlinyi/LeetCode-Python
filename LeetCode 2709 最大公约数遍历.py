MAXN = 10 ** 5 + 5
fac = [[] for _ in range(MAXN)]
for i in range(2, MAXN):
    if len(fac[i]) == 0:
        for j in range(i, MAXN, i):
            fac[j].append(i)


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        father = [i for i in range(n + MAXN)]

        def findFather(x: int) -> int:
            if father[x] != x:
                father[x] = findFather(father[x])
            return father[x]

        def Union(x: int, y: int):
            fatherX, fatherY = findFather(x), findFather(y)
            if fatherX != fatherY:
                father[fatherY] = fatherX

        for i, num in enumerate(nums):
            for p in fac[num]:
                Union(i, n + p)
        res = set()
        for i in range(n):
            res.add(findFather(i))
        if len(res) == 1:
            return True
        return False
