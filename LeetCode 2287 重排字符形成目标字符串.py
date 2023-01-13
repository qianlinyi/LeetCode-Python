from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt1, cnt2 = Counter(s), Counter(target)
        return min(cnt1[k] // v for k, v in cnt2.items())
