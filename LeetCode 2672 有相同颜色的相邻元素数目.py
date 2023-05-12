class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        a, cnt = [0] * (n + 2), 0
        for i, c in queries:
            i += 1
            if a[i]:
                cnt -= (a[i] == a[i - 1]) + (a[i] == a[i + 1])
            a[i] = c
            cnt += (a[i] == a[i - 1]) + (a[i] == a[i + 1])
            ans.append(cnt)
        return ans
