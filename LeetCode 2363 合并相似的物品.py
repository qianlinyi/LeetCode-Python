from sortedcontainers import SortedDict


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        cnt = SortedDict()
        for key, value in items1:
            cnt[key] = value
        for key, value in items2:
            if key in cnt:
                cnt[key] += value
            else:
                cnt[key] = value
        return [[k, v] for k, v in cnt.items()]
