import bisect


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1, 1001):
            y = 1 + bisect.bisect_left(range(1, 1000), z, key=lambda y: customfunction.f(x, y))
            if customfunction.f(x, y) == z:
                ans.append([x, y])
        return ans
