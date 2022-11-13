class Solution:
    def customSortString(self, order: str, s: str) -> str:
        p = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(list(s), key=lambda x: p.get(x, 27)))
