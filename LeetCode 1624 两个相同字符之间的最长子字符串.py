class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pos, ans = [-1 for _ in range(26)], -1
        for index, c in enumerate(s):
            if pos[ord(c) - ord('a')] == -1:
                pos[ord(c) - ord('a')] = index
            else:
                ans = max(ans, index - pos[ord(c) - ord('a')] - 1)
        return ans
