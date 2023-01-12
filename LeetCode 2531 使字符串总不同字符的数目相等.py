from collections import Counter


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        for x, v1 in cnt1.items():
            for y, v2 in cnt2.items():
                if x == y:
                    if len(cnt1) == len(cnt2):
                        return True
                elif len(cnt1) - (v1 == 1) + (y not in cnt1) == len(cnt2) - (v2 == 1) + (x not in cnt2):
                    return True
        return False
