class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        dp = [[0] * 26 for _ in range(m)]
        dp.append([m] * 26)
        for i in range(m - 1, -1, -1):
            for j in range(26):
                dp[i][j] = i if ord(t[i]) == j + ord('a') else dp[i + 1][j]
        add = 0
        for i in range(n):
            if dp[add][ord(s[i]) - ord('a')] == m:
                return False
            add = dp[add][ord(s[i]) - ord('a')] + 1
        return True
