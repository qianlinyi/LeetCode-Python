class Solution:
    def countEven(self, num: int) -> int:
        return sum(sum(list(map(int, list(str(_))))) % 2 == 0 for _ in range(1, num + 1))
