class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')
        sentence.append(sentence[0])
        return all(sentence[i][-1] == sentence[i + 1][0] for i in range(len(sentence) - 1))
