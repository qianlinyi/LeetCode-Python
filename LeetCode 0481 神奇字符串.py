class Solution:
    def magicalString(self, n: int) -> int:
        s = '122'
        index = 2
        while len(s) < n:
            if s[-1] == '2':
                s += (ord(s[index]) - ord('0')) * '1'
            else:
                s += (ord(s[index]) - ord('0')) * '2'
            index += 1
        return s[:n].count('1')
