from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.stream = ['' for _ in range(n + 1)]
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        stream_ = self.stream
        stream_[idKey] = value
        ans = []
        while self.ptr < len(stream_) and stream_[self.ptr]:
            ans.append(stream_[self.ptr])
            self.ptr += 1
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
