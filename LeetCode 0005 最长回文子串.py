class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx, pos, n = 0, -1, len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j + 1):
                if j - i < 3:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > mx:
                    mx = j - i + 1
                    pos = i
        return s[pos:pos + mx]
