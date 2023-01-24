class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        for idx, query in enumerate(queries):
            for point in points:
                x0, y0, r = query
                x1, y1 = point
                if (x1 - x0) ** 2 + (y1 - y0) ** 2 <= r ** 2:
                    ans[idx] += 1
        return ans
