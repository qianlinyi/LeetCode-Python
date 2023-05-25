class Solution:
    def oddString(self, words: List[str]) -> str:
        def get(word):
            diff = [0] * (len(word) - 1)
            for i in range(len(word) - 1):
                diff[i] = ord(word[i + 1]) - ord(word[i])
            return diff

        diff0 = get(words[0])
        diff1 = get(words[1])
        if diff0 == diff1:
            for i in range(2, len(words)):
                if diff0 != get(words[i]):
                    return words[i]
        return words[1] if diff0 == get(words[2]) else words[0]
