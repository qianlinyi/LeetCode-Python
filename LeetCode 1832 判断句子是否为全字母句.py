class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        cnt = Counter(sentence)
        return len(cnt.keys()) == 26
