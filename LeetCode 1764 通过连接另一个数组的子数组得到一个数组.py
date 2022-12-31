class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        n, m = len(nums), len(groups)
        idx1 = idx2 = 0
        while idx1 < n and idx2 < m:
            if nums[idx1:idx1 + len(groups[idx2])] == groups[idx2]:
                idx1 = idx1 + len(groups[idx2])
                idx2 += 1
            else:
                idx1 += 1
        return idx2 == m
