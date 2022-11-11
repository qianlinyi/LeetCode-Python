class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        return sum(s[:n // 2].count(_) for _ in vowel) == sum(s[n // 2:].count(_) for _ in vowel)
