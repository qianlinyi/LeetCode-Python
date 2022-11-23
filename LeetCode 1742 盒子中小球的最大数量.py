class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cnt = Counter()
        for i in range(lowLimit, highLimit + 1):
            cnt[sum(int(_) for _ in list(str(i)))] += 1
        return max(cnt.values())
