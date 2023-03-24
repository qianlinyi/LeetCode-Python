import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)
        while len(h) > 1:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            if a != b:
                heapq.heappush(h, a - b)
        return -h[0] if len(h) else 0