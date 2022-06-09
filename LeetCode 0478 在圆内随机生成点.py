import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        while True:
            x, y = random.uniform(-self.radius, self.radius), random.uniform(-self.radius, self.radius)  # 满足均匀随机分布
            if x ** 2 + y ** 2 <= self.radius ** 2:
                return [x + self.x_center, y + self.y_center]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
