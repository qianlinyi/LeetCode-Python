from typing import List
from collections import defaultdict


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dict = defaultdict()
        for i, piece in enumerate(pieces):
            dict[piece[0]] = i
        index = 0
        while index < len(arr):
            if arr[index] in dict:
                i, pos = 0, dict[arr[index]]
                while i < len(pieces[pos]) and pieces[pos][i] == arr[index]:
                    i, index = i + 1, index + 1
            else:
                break
        return index == len(arr)
