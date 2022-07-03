# 数学
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        x1, cnt1 = n, 1
        while x1 >= 10 and x1 // 10 % 10 >= x1 % 10:
            cnt1 += 1
            x1 //= 10
        x1 //= 10
        if x1 == 0:
            return -1

        targetDigit = x1 % 10
        x2, cnt2 = n, 0
        while x2 % 10 <= targetDigit:
            cnt2 += 1
            x2 //= 10
        x1 += x2 % 10 - targetDigit

        MAX_INT = 2 ** 31 - 1
        for i in range(cnt1):
            d = n % 10 if i != cnt2 else targetDigit
            if x1 > MAX_INT // 10 or x1 == MAX_INT // 10 and d > 7:
                return -1
            x1 = x1 * 10 + d
            n //= 10
        return x1
