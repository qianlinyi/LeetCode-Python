class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = set(dictionary)
        n = len(s)
        f = [0] * (n + 1)
        for i in range(n):
            f[i + 1] = f[i] + 1
            for j in range(i + 1):
                if s[j:i + 1] in d:
                    f[i + 1] = min(f[i + 1], f[j])
        return f[n]
