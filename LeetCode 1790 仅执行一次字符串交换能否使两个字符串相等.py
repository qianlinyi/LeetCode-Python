class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        else:
            pos = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    pos.append(i)
            if len(pos) == 2 and s1[pos[0]] == s2[pos[1]] and s1[pos[1]] == s2[pos[0]]:
                return True
            else:
                return False
