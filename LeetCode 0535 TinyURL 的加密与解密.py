# 自增
class Codec:
    def __init__(self):
        self.id2str = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        self.id += 1
        self.id2str[self.id] = longUrl
        return 'www.fuckyou.com*' + str(self.id)

    def decode(self, shortUrl: str) -> str:
        pos = shortUrl.find('*')
        id = int(shortUrl[pos + 1:])
        return self.id2str[id]
