class Solution:
    def rotatedDigits(self, n: int) -> int:
        goods, same, ans = [2, 5, 6, 9], [0, 1, 8], 0
        for i in range(1, n + 1):
            tmp = i
            flag1, flag2 = 1, 0
            while tmp:
                if tmp % 10 not in goods and tmp % 10 not in same:
                    flag1 = 0
                    break
                else:
                    if tmp % 10 in goods:
                        flag2 = 1
                    tmp //= 10
            if flag1 and flag2:
                ans += 1
        return ans
