class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = [0] * 26
        mx = l = r = 0
        n = len(s)
        while r < n:
            cnt[ord(s[r]) - ord('A')] += 1
            mx = max(mx, cnt[ord(s[r]) - ord('A')])
            if r - l + 1 - mx > k:
                cnt[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1
        return r - l
