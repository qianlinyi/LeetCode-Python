import heapq
from collections import Counter
from string import ascii_lowercase


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        f = Counter(s)
        h = [(f[c], c) for c in ascii_lowercase]
        heapq.heapify(h)

        t = []
        for _ in range(s.count('?')):
            f, c = h[0]
            t.append(c)
            heapq.heapreplace(h, (f + 1, c))
        t.sort()

        s = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] == '?':
                s[i] = t[j]
                j += 1
        return ''.join(s)
