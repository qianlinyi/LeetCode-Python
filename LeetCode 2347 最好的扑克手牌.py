from collections import Counter
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
            return 'Flush'
        cnt = Counter(ranks)
        flag = 0
        for k, v in cnt.items():
            if v >= 3:
                return 'Three of a Kind'
            elif v >= 2:
                flag = 1
        if flag:
            return 'Pair'
        return 'High Card'
