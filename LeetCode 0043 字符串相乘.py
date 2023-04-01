class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        ans = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                ans[i + j + 1] += x * int(num2[j])
        for i in range(m + n - 1, 0, -1):
            ans[i - 1] += ans[i] // 10
            ans[i] %= 10

        index = 1 if ans[0] == 0 else 0
        ans = ''.join(str(x) for x in ans[index:])
        return ans
