from typing import List


# DP,dp[i][j]表示以arr[i],arr[j]结尾的斐波那契数列的最大长度
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n, pos, ans = len(arr), {}, 0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dp[i][j] = 2
        for index, num in enumerate(arr):
            pos[num] = index
        for j in range(0, n):
            for k in range(j + 1, n):
                if arr[k] - arr[j] in pos:
                    i = pos[arr[k] - arr[j]]
                    dp[j][k] = max(dp[j][k], dp[i][j] + 1)
                    ans = max(ans, dp[j][k])
        return 0 if ans == 2 else ans
