import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = []
        for cls in classes:
            heapq.heappush(h, (cls[0] / cls[1] - (cls[0] + 1) / (cls[1] + 1), cls[0], cls[1]))
        while extraStudents:
            _, p, t = heapq.heappop(h)
            heapq.heappush(h, ((p + 1) / (t + 1) - (p + 2) / (t + 2), p + 1, t + 1))
            extraStudents -= 1
        return sum(x[1] / x[2] for x in h) / len(h)
