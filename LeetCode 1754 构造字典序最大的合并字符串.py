class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans = ''
        i, j, n, m = 0, 0, len(word1), len(word2)
        while i < n or j < m:
            if i < n and word1[i:] > word2[j:]:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1
        return ans
