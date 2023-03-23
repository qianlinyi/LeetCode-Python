class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def fuck(s: str) -> str:
            ss = ''
            for c in s:
                if c == '#':
                    if len(ss):
                        ss = ss[:-1]
                else:
                    ss += c
            return ss

        return fuck(s) == fuck(t)
