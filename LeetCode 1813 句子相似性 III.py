class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        word1, word2 = sentence1.split(), sentence2.split()
        i, j = 0, 0
        while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
            i += 1
        while j < len(word1) - i and j < len(word2) - i and word1[-j - 1] == word2[-j - 1]:
            j += 1
        return i + j == min(len(word1), len(word2))
