class MagicDictionary:

    def __init__(self):
        self.strDic = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for str in dictionary:
            self.strDic.add(str)

    def search(self, searchWord: str) -> bool:
        for i in range(searchWord):
            for j in range(0, 26):
                if searchWord[i] != chr(ord('a') + j):
                    word = searchWord[:i] + chr(ord('a') + j) + searchWord[i + 1:]
                    if word not in self.strDic:
                        return True
        return False
