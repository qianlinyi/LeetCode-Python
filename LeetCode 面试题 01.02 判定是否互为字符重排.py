from collections import defaultdict


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        cnt1, cnt2 = [0 for _ in range(26)], [0 for _ in range(26)]
        for c in s1:
            cnt1[ord(c) - ord('a')] += 1
        for c in s2:
            cnt2[ord(c) - ord('a')] += 1
        flag = True
        for i, v in enumerate(cnt1):
            if v != cnt2[i]:
                flag = False
                break
        return flag
