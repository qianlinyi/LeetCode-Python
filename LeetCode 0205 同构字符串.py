class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1, mp2 = dict(), dict()
        for i, c in enumerate(s):
            if c not in mp1:
                if t[i] in mp2:
                    return False
                mp1[c] = t[i]
                mp2[t[i]] = True
            else:
                if mp1[c] != t[i]:
                    return False
        return True
