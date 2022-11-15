class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        ans = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
        for i in range(k, n + 1):
            ans[i] = ans[i - 1]
            for j in range(0, i - k + 1):
                if dp[j][i - 1]:
                    ans[i] = max(ans[i], ans[j] + 1)
        return ans[-1]
