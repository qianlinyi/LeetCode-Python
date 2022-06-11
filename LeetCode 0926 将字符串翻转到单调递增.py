# 前缀和
# class Solution:
#     def minFlipsMonoIncr(self, s: str) -> int:
#         left, right, ans = [0 for _ in range(len(s))], [0 for _ in range(len(s))], len(s)
#         for i, c in enumerate(s):
#             if c == '0':
#                 left[i] += 1
#             if i > 0:
#                 left[i] += left[i - 1]
#         for i in range(len(s) - 1, -1, -1):
#             if s[i] == '1':
#                 right[i] += 1
#             if i < len(s) - 1:
#                 right[i] += right[i + 1]
#         for i in range(-1, len(s)):
#             ans = min(ans,
#                       (0 if i == -1 else i + 1 - left[i]) + (0 if i == len(s) - 1 else len(s) - i - 1 - right[i + 1]))
#         return ans

"""
DP
dp[i][0]=dp[i-1][0]+(s[i]==1)
dp[i][1]=min(dp[i-1][0],dp[i-1][1])+(s[i]==0)
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0, dp1 = 0, 0
        for c in s:
            dp0New, dp1New = dp0, min(dp0, dp1)
            if c == '1':
                dp0New += 1
            else:
                dp1New += 1
            dp0, dp1 = dp0New, dp1New
        return min(dp0, dp1)
