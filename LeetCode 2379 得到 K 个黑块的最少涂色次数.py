class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans = n
        for i in range(n - k + 1):
            ans = min(ans, blocks[i:i + k].count('W'))
        return ans
