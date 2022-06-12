from typing import List


# 构造双射
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str, pattern: str):
            mp = {}
            for a, b in zip(word, pattern):
                if a not in mp:
                    mp[a] = b
                elif mp[a] != b:
                    return False
            return True

        return [word for word in words if match(word, pattern) and match(pattern, word)]
