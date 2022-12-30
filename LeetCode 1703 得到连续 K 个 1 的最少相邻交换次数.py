import itertools
from typing import List


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        pre, zeros = -1, []
        for i, num in enumerate(nums):
            if num == 1:
                if pre != -1:
                    zeros.append(i - pre - 1)
                pre = i

        # 计算第一个窗口的解
        cost, left, right = 0, 0, k - 2
        for i in range(left, right + 1):
            cost += zeros[i] * min(i + 1, right - i + 1)

        minCost = cost
        pre = [0] + list(itertools.accumulate(zeros))
        while right < len(zeros) - 1:
            left += 1
            right += 1
            mid = left + right >> 1
            cost -= pre[mid] - pre[left - 1]
            cost += pre[right + 1] - pre[mid + k % 2]
            minCost = min(minCost, cost)
        return minCost
