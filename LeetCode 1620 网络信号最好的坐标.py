from typing import List


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        x_max = max(_[0] for _ in towers)
        y_max = max(_[1] for _ in towers)
        cx = cy = max_quality = 0
        for x in range(x_max + 1):
            for y in range(y_max + 1):
                quality = 0
                for tx, ty, q in towers:
                    d = (x - tx) ** 2 + (y - ty) ** 2
                    if d <= radius ** 2:
                        quality += int(q / (1 + d ** 0.5))
                if quality > max_quality:
                    cx, cy, max_quality = x, y, quality
        return [cx, cy]
