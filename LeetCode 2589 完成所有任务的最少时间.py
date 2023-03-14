class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1])
        run = [False] * (tasks[-1][1] + 1)
        for s, e, d in tasks:
            d -= sum(run[s:e + 1])
            if d > 0:
                for i in range(e, s - 1, -1):
                    if run[i]:
                        continue
                    run[i] = True
                    d -= 1
                    if d == 0:
                        break
        return sum(run)
