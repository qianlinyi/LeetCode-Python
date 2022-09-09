from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        layer = 0
        for log in logs:
            if log == '../':
                if layer == 0:
                    pass
                else:
                    layer -= 1
            elif log == './':
                pass
            else:
                layer += 1
        return layer
