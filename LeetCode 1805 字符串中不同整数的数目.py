import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        res = re.split(r'[a-z]+', word)
        return len(set([int(i) for i in res if i != '']))
