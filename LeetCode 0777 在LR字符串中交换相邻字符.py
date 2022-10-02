# 双指针
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        i = j = 0
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i < n and j < n:
                if start[i] != end[j]:
                    return False
                c = start[i]
                if c == 'L' and i < j or c == 'R' and i > j:
                    return False
                i += 1
                j += 1
        while i < n:
            if start[i] != 'X':
                return False
            i += 1
        while j < n:
            if end[j] != 'X':
                return False
            j += 1
        return True
