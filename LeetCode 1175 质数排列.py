import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        ans = 0
        for num in range(2, n + 1):
            flag = 1
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    flag = 0
                    break
            if flag:
                ans += 1
        return (math.factorial(ans) * math.factorial(n - ans)) % (10 ** 9 + 7)
