from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0 for _ in range(n)]
        for i, num in enumerate(code):
            if k == 0:
                ans[i] = 0
            elif k < 0:
                ans[i] = sum([code[(i + n) % n] for i in range(i - 1, i + k - 1, -1)])
            else:
                ans[i] = sum([code[i % n] for i in range(i + 1, i + k + 1)])
        return ans
