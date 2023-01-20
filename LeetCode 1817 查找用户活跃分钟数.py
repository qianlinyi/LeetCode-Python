from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        cnt = defaultdict(set)
        for log in logs:
            cnt[log[0]].add(log[1])
        ans = [0] * k
        for k, v in cnt.items():
            ans[len(v) - 1] += 1
        return ans
