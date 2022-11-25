from collections import deque
from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            q1, q2, flag = deque(s), deque(word), True
            while q1 and q2:
                fst, cnt1, cnt2 = q2[0], 0, 0
                if q1 and q1[0] != fst:
                    flag = False
                    break
                while q1 and q1[0] == fst:
                    q1.popleft()
                    cnt1 += 1
                while q2 and q2[0] == fst:
                    q2.popleft()
                    cnt2 += 1
                if cnt2 > cnt1 or (cnt1 != cnt2 and cnt1 < 3):
                    flag = False
                    break
            if flag and not q1 and not q2:
                ans += 1
        return ans
