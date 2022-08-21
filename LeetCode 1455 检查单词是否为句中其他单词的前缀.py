class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordlist = sentence.split(' ')
        for index, word in enumerate(wordlist):
            if word.find(searchWord) == 0:
                return index + 1
        return -1
