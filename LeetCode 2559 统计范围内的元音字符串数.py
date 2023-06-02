import itertools


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        change = [word[0] in ['a', 'e', 'i', 'o', 'u'] and word[-1] in ['a', 'e', 'i', 'o', 'u'] for word in words]
        pre = itertools.accumulate(change, initial=0)
        return [pre[query[1]] - pre[query[0]] for query in queries]
