import heapq


class Solution:
    def topKFrequent(self, words: List[str], x: int) -> List[str]:
        cnt = Counter(words)
        h = []
        for k, v in cnt.items():
            heapq.heappush(h, (-v, k))
        ans = []
        for _ in range(x):
            ans.append(heapq.heappop(h)[1])
        return ans