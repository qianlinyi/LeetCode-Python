from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        x = min(baseCosts)
        if x > target:
            return x
        can = [False] * (target + 1)
        ans = target * 2 - x
        for c in baseCosts:
            if c <= target:
                can[c] = True
            else:
                ans = min(ans, c)
        for c in toppingCosts:
            for count in range(2):
                for i in range(target, 0, -1):
                    if can[i] and i + c > target:
                        ans = min(ans, i + c)
                    if i - c > 0 and not can[i]:
                        can[i] = can[i - c]
        for i in range(ans - target + 1):
            if can[target - i]:
                return target - i
        return ans
