class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dis = 10 ** 5
        for point in points:
            if point[0] == x or point[1] == y:
                dis = min(dis, abs(x - point[0]) + abs(y - point[1]))
        if dis == 10 ** 5:
            return -1
        for idx, point in enumerate(points):
            if point[0] == x or point[1] == y:
                if abs(x - point[0]) + abs(y - point[1]) == dis:
                    return idx
