class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join([('' if i >= len(word1) else word1[i]) + ('' if i >= len(word2) else word2[i]) for i in
                        range(max(len(word2), len(word1)))])
