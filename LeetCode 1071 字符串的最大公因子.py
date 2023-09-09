import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = math.gcd(len(str1), len(str2))
        s = str1[:gcd]
        if str1 + str2 == str2 + str1:
            return s
        return ""
