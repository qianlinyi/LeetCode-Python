import math


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 1
        for i in range(1, int(math.sqrt(2 * n))):
            if n - i * (i + 1) // 2 >= 0 and (n - i * (i + 1) // 2) % (i + 1) == 0:
                ans += 1
        return ans
