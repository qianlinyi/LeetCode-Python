from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        cnt, ans = [[] for _ in range(len(groupSizes) + 1)], []
        for index, value in enumerate(groupSizes):
            cnt[value].append(index)
        for i in range(1, len(groupSizes) + 1):
            if len(cnt[i]) == 0:
                continue
            for j in range(len(cnt[i]) // i):
                ans.append([cnt[i][i * j + k] for k in range(i)])
        return ans
