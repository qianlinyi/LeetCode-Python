from bisect import bisect_right


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
        ans = len(words)
        for word in words:
            if len(word) > len(s):
                ans -= 1
                continue
            p = -1
            for c in word:
                ps = pos[c]
                j = bisect_right(ps, p)
                if j == len(ps):
                    ans -= 1
                    break
                p = ps[j]
        return ans
