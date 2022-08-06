from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in words:
            for j in words:
                if i == j:
                    continue
                if j.find(i) != -1:
                    ans.append(i)
                    break
        return ans
