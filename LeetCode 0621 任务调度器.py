class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        mx = max(cnt.values())
        mxCnt = sum(1 for v in cnt.values() if v == mx)
        return max((mx - 1) * (n + 1) + mxCnt, len(tasks))