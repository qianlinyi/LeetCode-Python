class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = {}
        ans = 0
        cur = trie
        for c in pref:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = {}
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    break
                cur = cur[c]
                if '#' in cur:
                    ans += 1
                    break
        return ans
