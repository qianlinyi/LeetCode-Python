from collections import deque
from itertools import pairwise
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        g = [[] for _ in range(n)]
        inDeg = [0] * n
        for sequence in sequences:
            for x, y in pairwise(sequence):
                g[x - 1].append(y - 1)
                inDeg[y - 1] += 1

        q = deque([i for i, d in enumerate(inDeg) if d == 0])
        while q:
            if len(q) > 1:
                return False
            x = q.popleft()
            for y in g[x]:
                inDeg[y] -= 1
                if inDeg[y] == 0:
                    q.append(y)
        return True
