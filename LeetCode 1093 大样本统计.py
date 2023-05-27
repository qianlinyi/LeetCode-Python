from collections import Counter


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        cnt = Counter()
        for i in range(256):
            if count[i]:
                cnt[i] = count[i]
        l = sum(cnt.values())
        minimum = min(cnt.keys())
        maximum = max(cnt.keys())
        mean = sum(k * v for k, v in cnt.items()) / l
        mx = max(cnt.values())
        for x in cnt.keys():
            if cnt[x] == mx:
                mode = x
        keys = list(cnt.keys())

        def fuck(x):
            while x:
                for i in range(256):
                    if x > cnt[i]:
                        x -= cnt[i]
                    else:
                        return i

        if l % 2:
            median = fuck(l // 2 + 1)
        else:
            ans1 = fuck(l // 2)
            ans2 = fuck(l // 2 + 1)
            median = (ans1 + ans2) / 2
        return [minimum, maximum, mean, median, mode]
