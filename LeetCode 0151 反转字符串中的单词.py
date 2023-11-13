class Solution:

    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        return ' '.join([_ for _ in s if len(_)][::-1])
