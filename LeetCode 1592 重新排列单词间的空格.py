class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        num = text.count(' ')
        if len(words) == 1:
            return ''.join(words) + num * ' '
        ans = ''
        for word in words:
            ans += word + (num // (len(words) - 1)) * ' '
        ans = ans.rstrip()
        ans += (num % (len(words) - 1)) * ' '
        return ans
