class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans, cnt1, cnt2 = [], [0] * 26, [0] * 26
        n, m = len(s), len(p)
        if m > n:
            return ans
        for i in range(m):
            cnt1[ord(s[i]) - ord('a')] += 1
            cnt2[ord(p[i]) - ord('a')] += 1
        if all(cnt1[_] == cnt2[_] for _ in range(26)):
            ans.append(0)
        for i in range(m, n):
            cnt1[ord(s[i - m]) - ord('a')] -= 1
            cnt1[ord(s[i]) - ord('a')] += 1
            if all(cnt1[_] == cnt2[_] for _ in range(26)):
                ans.append(i - m + 1)
        return ans
