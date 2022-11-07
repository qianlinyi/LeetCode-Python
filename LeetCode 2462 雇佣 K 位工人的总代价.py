from queue import PriorityQueue
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q = PriorityQueue()
        n = len(costs)
        l, r = 0, n - 1
        while l < candidates:
            q.put((costs[l], l))
            l += 1
        while r > l and n - r - 1 < candidates:
            q.put((costs[r], r))
            r -= 1
        ans = 0
        for _ in range(k):
            cost, index = q.get()
            ans += cost
            if index < l:
                if l <= r:  # 判断指针是否相遇
                    q.put((costs[l], l))
                    l += 1
            else:
                if l <= r:
                    q.put((costs[r], r))
                    r -= 1
        return ans
