class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        cnt = Counter()
        ans = 0
        k = 0
        for value, label in sorted(zip(values, labels), key=lambda x: -x[0]):
            if k < numWanted and cnt[label] < useLimit:
                cnt[label] += 1
                ans += value
                k += 1
        return ans