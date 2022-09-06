from collections import defaultdict


# 分别计算每个字符的贡献
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)

        ans = 0
        for arr in pos.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                ans += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return ans
