class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        ans = 0
        flag = False
        for k in cnt.keys():
            if k[0] == k[1]:
                while cnt[k] > 1:
                    ans += 4
                    cnt[k] -= 2
                if cnt[k]:
                    flag = True
            else:
                while cnt[k] and cnt[k[::-1]]:
                    ans += 4
                    cnt[k] -= 1
                    cnt[k[::-1]] -= 1
        return ans + 2 if flag else ans
