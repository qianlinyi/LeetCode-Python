from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        ans = sorted(zip(nums, cost))
        n = len(ans)
        sum1 = [0 for _ in range(n)]
        sum2 = [0 for _ in range(n)]
        for i in range(n):
            sum1[i] = ans[i][1] if i == 0 else ans[i][1] + sum1[i - 1]
            sum2[i] = ans[i][0] * ans[i][1] if i == 0 else ans[i][0] * ans[i][1] + sum2[i - 1]
        res = 10 ** 18
        for i in range(n):
            x = ans[i][0]
            if i == 0:
                res = min(res, abs(sum1[n - 1] * x - sum2[n - 1]))
            else:
                res = min(res,
                          abs((sum1[n - 1] - sum1[i - 1]) * x - (sum2[n - 1] - sum2[i - 1]) - (sum1[i - 1] * x - sum2[
                              i - 1])))
        return res
