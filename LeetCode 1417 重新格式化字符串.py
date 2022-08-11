class Solution:
    def reformat(self, s: str) -> str:
        digit, alpha, ans = '', '', ''
        for c in s:
            if c.isdigit():
                digit += c
            if c.isalpha():
                alpha += c
        if abs(len(digit) - len(alpha)) > 1:
            return ''
        n = min(len(digit), len(alpha))
        for i in range(n):
            ans += digit[i] + alpha[i]
        if len(digit) > n:
            ans += digit[-1]
        if len(alpha) > n:
            ans = alpha[-1] + ans
        return ans
