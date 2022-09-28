# 最小堆
from queue import PriorityQueue


class Solution1:
    def getKthMagicNumber(self, k: int) -> int:
        factors = [3, 5, 7]
        seen = {1}
        heap = PriorityQueue()
        heap.put(1)
        for i in range(k - 1):
            cur = heap.get()
            for factor in factors:
                if (nxt := cur * factor) not in seen:
                    seen.add(nxt)
                    heap.put(nxt)
        return heap.get()


# 动态规划
class Solution2:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [0 for _ in range(k + 1)]
        dp[1] = 1
        p3 = p5 = p7 = 1
        for i in range(2, k + 1):
            num3, num5, num7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
            dp[i] = min(num3, num5, num7)
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
            if dp[i] == num7:
                p7 += 1
        return dp[k]
