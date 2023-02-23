from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            for j in range(len(ans) - 1, -1, -1):
                ans.append(ans[j] | (1 << (i - 1)))
        return ans
