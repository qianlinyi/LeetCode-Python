from collections import Counter


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cnt, n, m = Counter(wordDict), len(s), max(len(word) for word in wordDict)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            for j in range(0, i):
                if dp[j] and cnt[s[j:i]]:
                    dp[i] = True
                    break
        return dp[n]
