class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(set(word).issubset(allowed) for word in words)
