class Solution:

    def maxSpending(self, values: List[List[int]]) -> int:
        a = sorted(x for row in values for x in row)
        return sum(x * i for i, x in enumerate(a, 1))
